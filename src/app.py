"""Bootstrap do aplicativo LIBRYNO v2.0.

╔══════════════════════════════════════════════════════════════════╗
║  REGRAS DE AUTENTICAÇÃO OBRIGATÓRIAS                           ║
║                                                                  ║
║  1. O Libryno SÓ funciona com login via API OrdoB.              ║
║  2. NÃO existe modo offline — API deve estar acessível.         ║
║  3. NÃO existe cadastro/registro dentro do Libryno.             ║
║  4. Conta OrdoB é criada em ordob.com/cadastro.                 ║
║  5. Dados locais (livros, leitores) ficam APENAS na máquina.    ║
║  6. Token é validado no startup e a cada hora.                   ║
║  7. Auto-update verifica versão no startup (background).         ║
╚══════════════════════════════════════════════════════════════════╝
"""
import atexit
import sys

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox, QProgressDialog
from PySide6.QtCore import QTimer

from src.auth.license import (
    auto_detect_premium,
    check_existing_license,
    start_license_monitoring,
    stop_license_monitoring,
    validate_session_token,
)
from src.auth.ordob_client import client
from src.auth.session import session
from src.config import Config
from src.core.migrations import setup_database
from src.core.seed import seed_demo_data
from src.sync.sync_manager import sync_manager
from src.ui.i18n.translator import _load_locale, set_locale
from src.ui.screens.home import HomeScreen
from src.ui.screens.login import LoginScreen
from src.ui.themes.theme_manager import (
    apply_system_theme,
)
from src.updater import auto_updater
from src.utils.logger import logger

_sse_stop_event = None
_main_window = None
_login_window = None
_app = None


def run():
    global _app
    logger.info("LIBRYNO v{} starting...", Config.APP_VERSION)

    _app = QtWidgets.QApplication(sys.argv)
    _app.setApplicationName(Config.APP_NAME)
    _app.setApplicationVersion(Config.APP_VERSION)
    _app.setWindowIcon(QtGui.QIcon(Config.resource_path("img/logoicone.png")))

    _load_locale("pt_BR")
    _load_locale("en")
    set_locale("pt_BR")

    apply_system_theme(_app)

    setup_database()

    # ─── AUTH: Verificar sessão salva primeiro ───
    # Se há token salvo, validar contra API antes de mostrar login.
    if session.is_authenticated:
        logger.info("Found saved session, validating...")
        if _validate_saved_session():
            logger.info("Session valid — auto-login")
            _on_auth_success()
            atexit.register(cleanup)
            # Iniciar auto-update check em background após login
            QTimer.singleShot(3000, _start_background_update_check)
            sys.exit(_app.exec_())
        else:
            logger.info("Session invalid — showing login")
            session.logout()

    # Sem sessão válida — mostrar login
    _show_login()

    atexit.register(cleanup)
    sys.exit(_app.exec_())


def _validate_saved_session() -> bool:
    """Valida token salvo contra a API OrdoB (silencioso)."""
    if not session.token:
        return False

    # Verificar conectividade primeiro
    if not client.health_check():
        logger.warning("API unreachable — cannot validate saved session")
        return False

    # Validar token
    return validate_session_token()


def _validate_session_or_prompt_login() -> bool:
    """Valida token salvo — mostra prompt se inválido."""
    logger.info("Validating saved session token against OrdoB API...")

    if not client.health_check():
        logger.warning("OrdoB API unreachable during startup validation")
        reply = QMessageBox.question(
            None,
            "Servidor Indisponível",
            "O servidor OrdoB está inacessível.\n\n"
            "O LIBRYNO requer autenticação para funcionar.\n"
            "Deseja tentar novamente?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes,
        )
        if reply == QMessageBox.StandardButton.Yes:
            return _validate_session_or_prompt_login()
        else:
            QMessageBox.critical(
                None,
                "Acesso Negado",
                "LIBRYNO requer conexão com o servidor OrdoB.\n"
                "O aplicativo será encerrado.",
            )
            return False

    if validate_session_token():
        logger.info("Session token valid — proceeding")
        _on_auth_success()
        return True
    else:
        logger.warning("Session token invalid/expired — forcing re-login")
        session.logout()
        QMessageBox.warning(
            None,
            "Sessão Expirada",
            "Sua sessão expirou ou foi revogada.\n"
            "Por favor, faça login novamente com sua conta OrdoB.",
        )
        return False


def _on_auth_success():
    """Chamado após autenticação bem-sucedida."""
    global _main_window, _login_window

    # Auto-detectar licença Premium
    auto_detect_premium()
    check_existing_license()
    start_license_monitoring()

    # Seed só roda após autenticação
    seed_demo_data()

    _main_window = HomeScreen()
    _main_window.show()
    _start_realtime_notifications()
    sync_manager.sync_start(Config.SYNC_INTERVAL)

    # Iniciar verificação de atualizações em background
    QTimer.singleShot(3000, _start_background_update_check)


def _show_login():
    global _login_window
    _login_window = LoginScreen(on_success=_show_home)
    _login_window.show()


def _show_home():
    global _sse_stop_event, _main_window, _login_window
    if _login_window:
        _login_window.close()
        _login_window = None
    _on_auth_success()


def _start_background_update_check():
    """Inicia verificação de atualizações em background."""
    if not Config.AUTO_UPDATE_ENABLED:
        logger.info("Auto-update disabled, skipping check")
        return

    if not Config.AUTO_UPDATE_ENABLED:
        return

    logger.info("Starting background update check...")
    auto_updater.check_and_notify(
        on_update_available=lambda info: _show_update_available_dialog(info),
        on_no_update=lambda: logger.info("No updates available"),
        on_error=lambda reason: logger.warning("Update check failed: {}", reason),
    )


def _show_update_available_dialog(info: dict):
    """Mostra dialog de atualização disponível."""
    if _main_window is None:
        logger.warning("Main window not ready, cannot show update dialog")
        return

    current = info.get("current_version", "?")
    latest = info.get("latest_version", "?")
    notes = info.get("release_notes", "")

    msg = QMessageBox(_main_window)
    msg.setWindowTitle("Atualização Disponível")
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText(f"Nova versão {latest} disponível! (Atual: {current})")
    msg.setInformativeText(
        f"Deseja baixar e instalar a atualização agora?\n\n"
        f"Novidades:\n{notes[:500]}..."
    )
    msg.setStandardButtons(
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
    msg.setDefaultButton(QMessageBox.StandardButton.Yes)

    reply = msg.exec()

    if reply == QMessageBox.StandardButton.Yes:
        _run_update_with_progress(info)


def _run_update_with_progress(info: dict):
    """Executa atualização com barra de progresso."""
    if _main_window is None:
        return

    progress = QProgressDialog("Baixando atualização...", "Cancelar", 0, 100, _main_window)
    progress.setWindowTitle("Atualizando Libryno")
    progress.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
    progress.setMinimumDuration(0)
    progress.setAutoClose(False)
    progress.setAutoReset(False)

    from src.updater import UpdateProgress
    from src.updater import auto_updater

    def on_start():
        progress.setLabelText("Iniciando download...")
        progress.setValue(0)

    def on_progress(downloaded: int, total: int):
        if total > 0:
            percent = int((downloaded / total) * 100)
            progress.setValue(percent)
            progress.setLabelText(f"Baixando... {percent}% ({_format_bytes(downloaded)}/{_format_bytes(total)})")

    def on_complete(success: bool, message: str):
        progress.close()
        if success:
            QMessageBox.information(
                _main_window,
                "Atualização Concluída",
                "A atualização foi instalada com sucesso!\n"
                "O Libryno será reiniciado para aplicar as mudanças."
            )
            # Reiniciar app
            QtCore.QCoreApplication.quit()
            QtCore.QProcess.startDetached(sys.executable, sys.argv)
        else:
            QMessageBox.warning(
                _main_window,
                "Erro na Atualização",
                f"Falha ao atualizar: {message}\n\n"
                "Você pode baixar manualmente em:\n"
                f"https://github.com/ordo-b/LIBRYNO/releases/latest"
            )

    from src.updater import UpdateProgress
    updater_progress = UpdateProgress(
        on_start=on_start,
        on_progress=on_progress,
        on_complete=on_complete,
    )

    # Executa em thread separada
    from src.updater import auto_updater
    def update_worker():
        auto_updater.apply_update(info, updater_progress)

    import threading
    threading.Thread(target=update_worker, daemon=True, name="UpdateApply").start()


def _format_bytes(bytes_val: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_val < 1024:
            return f"{bytes_val:.1f} {unit}"
        bytes_val /= 1024
    return f"{bytes_val:.1f} TB"


def _on_notification(data: dict):
    """Callback para notificações SSE em tempo real."""
    logger.info("SSE notification received: {}", data.get("type") or "unknown")
    try:
        from src.features.notifications import NotificationsCRUD
        if data.get("type") == "unread_count":
            count = data.get("data", 0)
            NotificationsCRUD.create(
                titulo="Nova notificação",
                mensagem=f"Você tem {count} notificação(ões) não lida(s).",
                tipo="sse_alert",
            )
        elif "ticket" in str(data.get("type", "")):
            NotificationsCRUD.create(
                titulo="Atualização de ticket",
                mensagem=data.get("data", {}).get("message_preview", "Nova mensagem"),
                tipo="sse_ticket",
            )
    except Exception as e:
        logger.error("Error processing SSE notification: {}", e)


def _start_realtime_notifications():
    """Inicia streaming SSE de notificações em tempo real."""
    global _sse_stop_event
    if session.is_authenticated and session.token:
        try:
            _sse_stop_event = client.stream_notifications(
                token=session.token,
                on_message=_on_notification,
                on_error=_on_sse_error,
            )
            logger.info("Realtime notifications started")
        except Exception as e:
            logger.error("Failed to start SSE: {}", e)
    return _sse_stop_event


def _on_sse_error(error: str):
    """Callback de erro para SSE."""
    logger.warning("SSE error: {}", error)


def cleanup():
    """Cleanup ao encerrar aplicativo."""
    stop_license_monitoring()
    sync_manager.sync_stop()
    if _sse_stop_event:
        _sse_stop_event.set()
    logger.info("LIBRYNO shutdown complete")
