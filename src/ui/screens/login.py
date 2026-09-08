"""Tela de Login — Autenticação Obrigatória via OrdoB.

REGRAS:
1. NÃO existe cadastro/registro dentro do Libryno.
2. O usuário DEVE ter conta OrdoB (ordob.com) para usar o Libryno.
3. Login envia email/senha para a API OrdoB — validação server-side.
4. Sem autenticação = sem acesso ao aplicativo.
5. Dados locais (livros, leitores) ficam apenas na máquina do usuário.

UX MELHORADA:
- "Lembrar email" — salva o último email usado (QSettings)
- Show/hide password — botão de olho no campo de senha
- Loading spinner — indica autenticação em andamento
- "Esqueci minha senha" — link para reset no OrdoB
- Status de conexão — mostra se servidor está acessível
- Auto-focus no campo de email
- Login via navegador — alternativa sem digitar senha
"""
import time
import webbrowser

from PySide6 import QtGui
from PySide6.QtCore import Qt, QSettings, QThread, QTimer, Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QProgressBar,
    QVBoxLayout,
    QWidget,
)

from src.auth.license import check_existing_license
from src.auth.ordob_client import client
from src.auth.session import session
from src.config import Config
from src.ui.i18n.translator import t


class _LoginWorker(QThread):
    """Worker thread para login — evita congelar a UI."""
    finished = Signal(dict)
    error = Signal(str)

    def __init__(self, email: str, password: str):
        super().__init__()
        self.email = email
        self.password = password

    def run(self):
        try:
            # Login direto — health check é rápido e já testamos antes
            result = client.login(self.email, self.password)
            if result:
                self.finished.emit(result)
            else:
                self.error.emit("login.error")
        except Exception as e:
            self.error.emit("login.error")


class LoginScreen(QMainWindow):
    """Tela de login — única forma de acessar o Libryno."""

    def __init__(self, on_success=None):
        super().__init__()
        self.on_success = on_success
        self._worker = None
        self._settings = QSettings("OrdoB", "Libryno")
        self.setWindowTitle(t("login.title"))
        self.setFixedSize(750, 640)
        self.setWindowIcon(QtGui.QIcon(Config.resource_path("img/logoicone.png")))
        self._build_ui()
        self._restore_email()
        # Verificar servidor ao abrir
        QTimer.singleShot(300, self._check_server)

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # ─── LADO ESQUERDO: branding ───
        left = QFrame()
        left.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #16213e, stop:1 #0f3460);
                border-radius: 0px;
            }
        """)
        left_layout = QVBoxLayout(left)
        left_layout.setAlignment(Qt.AlignCenter)
        left_layout.setContentsMargins(30, 40, 30, 40)

        # Logo (logotipo novo — logo + nome)
        brand_logo = QLabel()
        brand_logo.setAlignment(Qt.AlignCenter)
        brand_pixmap = QtGui.QPixmap(Config.resource_path("img/logonome.png"))
        if not brand_pixmap.isNull():
            brand_pixmap = brand_pixmap.scaledToWidth(
                230, Qt.TransformationMode.SmoothTransformation
            )
            brand_logo.setPixmap(brand_pixmap)
        brand_logo.setStyleSheet("background: transparent;")
        left_layout.addWidget(brand_logo)

        subtitle = QLabel(t("login.login_with_ordob"))
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet(
            "font-size: 14px; color: #a0a0a0; background: transparent;"
        )
        left_layout.addWidget(subtitle)

        left_layout.addSpacing(20)

        auth_notice = QLabel(t("login.auth_required"))
        auth_notice.setAlignment(Qt.AlignCenter)
        auth_notice.setWordWrap(True)
        auth_notice.setStyleSheet(
            "font-size: 11px; color: #FFD700; background: transparent; "
            "padding: 10px 16px; "
            "border: 1px solid #FFD700; border-radius: 6px;"
        )
        left_layout.addWidget(auth_notice)

        left_layout.addSpacing(20)

        self._status_label = QLabel(t("login.checking_server"))
        self._status_label.setAlignment(Qt.AlignCenter)
        self._status_label.setStyleSheet(
            "font-size: 12px; color: #a0a0a0; background: transparent;"
        )
        left_layout.addWidget(self._status_label)

        self._progress = QProgressBar()
        self._progress.setRange(0, 0)
        self._progress.setFixedHeight(3)
        self._progress.setTextVisible(False)
        self._progress.setStyleSheet("""
            QProgressBar { background-color: transparent; border: none; }
            QProgressBar::chunk { background-color: #5CE1E6; }
        """)
        self._progress.hide()
        left_layout.addWidget(self._progress)

        left_layout.addStretch()
        layout.addWidget(left, 1)

        # ─── LADO DIREITO: formulário ───
        right = QFrame()
        right.setStyleSheet("QFrame { background-color: #1a1a2e; }")
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(40, 40, 40, 30)
        right_layout.setSpacing(10)

        title = QLabel(t("login.title"))
        title.setStyleSheet(
            "font-size: 22px; font-weight: bold; color: #ffffff; "
            "background: transparent; margin-bottom: 2px;"
        )
        right_layout.addWidget(title)

        info_label = QLabel(t("login.no_account_info"))
        info_label.setWordWrap(True)
        info_label.setStyleSheet(
            "font-size: 12px; color: #a0a0a0; background: transparent; "
            "margin-bottom: 8px;"
        )
        right_layout.addWidget(info_label)

        # Email
        email_label = QLabel(t("login.email"))
        email_label.setStyleSheet("color: #cccccc; font-size: 12px; background: transparent;")
        right_layout.addWidget(email_label)

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText(t("login.email_placeholder"))
        self.input_email.setFixedHeight(44)
        self.input_email.setStyleSheet("""
            QLineEdit { background-color: #16213e; color: #ffffff; border: 1px solid #333;
                border-radius: 6px; padding: 0 12px; font-size: 14px; }
            QLineEdit:focus { border: 1px solid #5CE1E6; }
        """)
        right_layout.addWidget(self.input_email)

        # Senha
        pass_label = QLabel(t("login.password"))
        pass_label.setStyleSheet("color: #cccccc; font-size: 12px; background: transparent;")
        right_layout.addWidget(pass_label)

        pass_container = QHBoxLayout()
        pass_container.setSpacing(0)

        self.input_pass = QLineEdit()
        self.input_pass.setPlaceholderText(t("login.password_placeholder"))
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setFixedHeight(44)
        self.input_pass.returnPressed.connect(self._do_login)
        self.input_pass.setStyleSheet("""
            QLineEdit { background-color: #16213e; color: #ffffff; border: 1px solid #333;
                border-radius: 6px; padding: 0 12px; font-size: 14px; }
            QLineEdit:focus { border: 1px solid #5CE1E6; }
        """)
        pass_container.addWidget(self.input_pass)

        self._btn_show_pass = QPushButton("👁")
        self._btn_show_pass.setFixedSize(44, 44)
        self._btn_show_pass.setCheckable(True)
        self._btn_show_pass.setStyleSheet("""
            QPushButton { background-color: #16213e; border: 1px solid #333;
                border-radius: 6px; font-size: 16px; margin-left: 6px; }
            QPushButton:hover { background-color: #1a2744; }
            QPushButton:checked { background-color: #0f3460; border-color: #5CE1E6; }
        """)
        self._btn_show_pass.toggled.connect(self._toggle_password_visibility)
        pass_container.addWidget(self._btn_show_pass)
        right_layout.addLayout(pass_container)

        # Lembrar email
        self._remember_check = QCheckBox(t("login.remember_email"))
        self._remember_check.setStyleSheet(
            "color: #a0a0a0; font-size: 12px; background: transparent; margin-top: 4px;"
        )
        self._remember_check.stateChanged.connect(self._on_remember_changed)
        right_layout.addWidget(self._remember_check)

        right_layout.addSpacing(6)

        # Botão de login
        self._btn_login = QPushButton(t("login.enter"))
        self._btn_login.setFixedHeight(48)
        self._btn_login.setCursor(Qt.PointingHandCursor)
        self._btn_login.setStyleSheet("""
            QPushButton { background-color: #5CE1E6; color: #1a1a2e; border: none;
                border-radius: 6px; font-size: 16px; font-weight: bold; }
            QPushButton:hover { background-color: #4dd0d5; }
            QPushButton:pressed { background-color: #3bbcc2; }
            QPushButton:disabled { background-color: #333; color: #666; }
        """)
        self._btn_login.clicked.connect(self._do_login)
        right_layout.addWidget(self._btn_login)

        # Links auxiliares
        links_layout = QHBoxLayout()

        btn_forgot = QPushButton(t("login.forgot_password"))
        btn_forgot.setFlat(True)
        btn_forgot.setStyleSheet(
            "color: #5CE1E6; font-size: 12px; background: transparent; "
            "border: none; text-decoration: underline;"
        )
        btn_forgot.setCursor(Qt.PointingHandCursor)
        btn_forgot.clicked.connect(self._open_forgot_password)
        links_layout.addWidget(btn_forgot)

        links_layout.addStretch()

        btn_create = QPushButton(t("login.create_account_ordob"))
        btn_create.setFlat(True)
        btn_create.setStyleSheet(
            "color: #5CE1E6; font-size: 12px; background: transparent; "
            "border: none; text-decoration: underline;"
        )
        btn_create.setCursor(Qt.PointingHandCursor)
        btn_create.clicked.connect(self._open_ordob_signup)
        links_layout.addWidget(btn_create)

        right_layout.addLayout(links_layout)

        # ─── ENTRAR COM ORDOB ───
        right_layout.addSpacing(8)

        btn_ordob = QPushButton("🌐 Entrar com OrdoB.com")
        btn_ordob.setFixedHeight(44)
        btn_ordob.setCursor(Qt.PointingHandCursor)
        btn_ordob.setStyleSheet("""
            QPushButton { background-color: #ffffff; color: #333333; border: none;
                border-radius: 6px; font-size: 14px; font-weight: bold; }
            QPushButton:hover { background-color: #f0f0f0; }
        """)
        btn_ordob.clicked.connect(self._login_with_ordob)
        right_layout.addWidget(btn_ordob)

        sep = QLabel("ou")
        sep.setAlignment(Qt.AlignCenter)
        sep.setStyleSheet("color: #666; font-size: 12px; background: transparent; margin: 4px 0;")
        right_layout.addWidget(sep)

        right_layout.addStretch()

        version = QLabel(f"v{Config.APP_VERSION}")
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet("color: #666666; font-size: 11px; background: transparent;")
        right_layout.addWidget(version)

        layout.addWidget(right, 1)

    # ─── Server check ───

    def _check_server(self):
        """Verifica se o servidor OrdoB está acessível (em background)."""
        class _HealthWorker(QThread):
            result = Signal(bool)
            def run(self):
                self.result.emit(client.health_check())

        self._health = _HealthWorker()
        self._health.result.connect(self._on_server_result)
        self._health.start()

    def _on_server_result(self, online: bool):
        if online:
            self._status_label.setText(t("login.server_online"))
            self._status_label.setStyleSheet(
                "font-size: 12px; color: #44ff44; background: transparent;"
            )
        else:
            self._status_label.setText(t("login.server_offline"))
            self._status_label.setStyleSheet(
                "font-size: 12px; color: #ff4444; background: transparent;"
            )

    # ─── Settings ───

    def _restore_email(self):
        remember = self._settings.value("login/remember_email", False, type=bool)
        self._remember_check.setChecked(remember)
        if remember:
            saved = self._settings.value("login/email", "", type=str)
            if saved:
                self.input_email.setText(saved)

    def _on_remember_changed(self, state):
        if state:
            self._settings.setValue("login/remember_email", True)
            self._settings.setValue("login/email", self.input_email.text().strip())
        else:
            self._settings.setValue("login/remember_email", False)
            self._settings.remove("login/email")

    def _toggle_password_visibility(self, checked):
        if checked:
            self.input_pass.setEchoMode(QLineEdit.Normal)
            self._btn_show_pass.setText("🙈")
        else:
            self.input_pass.setEchoMode(QLineEdit.Password)
            self._btn_show_pass.setText("👁")

    # ─── Loading ───

    def _set_loading(self, loading: bool):
        self._btn_login.setEnabled(not loading)
        self.input_email.setEnabled(not loading)
        self.input_pass.setEnabled(not loading)

        if loading:
            self._progress.show()
            self._status_label.setText(t("login.authenticating"))
            self._status_label.setStyleSheet(
                "font-size: 12px; color: #5CE1E6; background: transparent;"
            )
            self._btn_login.setText(t("login.authenticating"))
        else:
            self._progress.hide()
            self._btn_login.setText(t("login.enter"))

    # ─── Login ───

    def _do_login(self):
        email = self.input_email.text().strip()
        password = self.input_pass.text().strip()

        if not email or not password:
            QMessageBox.warning(
                self, t("messages.warning"), t("messages.fields_required")
            )
            return

        if self._remember_check.isChecked():
            self._settings.setValue("login/email", email)

        self._set_loading(True)

        self._worker = _LoginWorker(email, password)
        self._worker.finished.connect(self._on_login_success)
        self._worker.error.connect(self._on_login_error)
        self._worker.start()

        # Safety timeout — se worker não responder em 30s, desbloquear
        QTimer.singleShot(30000, self._safety_timeout)

    def _safety_timeout(self):
        """Força desbloqueio se worker não respondeu."""
        if self._worker and self._worker.isRunning():
            self._set_loading(False)
            self._status_label.setText(t("login.server_offline"))
            self._status_label.setStyleSheet(
                "font-size: 12px; color: #ff4444; background: transparent;"
            )
            QMessageBox.critical(
                self,
                t("messages.error"),
                t("login.server_unreachable"),
            )

    def _on_login_success(self, result: dict):
        self._set_loading(False)

        token = result.get("token", "")
        user = result.get("user", {})
        session.login(token, user)

        check_existing_license()

        self._status_label.setText(t("login.success"))
        self._status_label.setStyleSheet(
            "font-size: 12px; color: #44ff44; background: transparent;"
        )

        QMessageBox.information(self, t("messages.success"), t("login.success"))
        self.close()
        if self.on_success:
            self.on_success()

    def _on_login_error(self, msg_key: str):
        self._set_loading(False)
        # Erro de autenticação — o estado real do servidor é mostrado
        # pelo health check; não force "online" aqui.
        self._status_label.setText("")
        self._status_label.setStyleSheet(
            "font-size: 12px; background: transparent;"
        )
        # Mensagem de erro mais detalhada
        reply = QMessageBox.critical(
            self, t("messages.error"),
            t(msg_key) + "\n\n" +
            "Possíveis causas:\n"
            "• Email ou senha incorretos\n"
            "• Conta ainda não criada em ordob.com/cadastro\n"
            "\n" +
            "Deseja abrir o site do OrdoB para verificar?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes,
        )
        if reply == QMessageBox.StandardButton.Yes:
            webbrowser.open("https://ordob.com/login")

    # ─── External links ───

    def _open_ordob_signup(self):
        webbrowser.open("https://ordob.com/cadastro")
        QMessageBox.information(
            self,
            t("login.create_account_ordob"),
            t("login.create_account_info"),
        )

    def _open_forgot_password(self):
        """Envia email de redefinição de senha no OrdoB."""
        email = self.input_email.text().strip()
        if not email:
            # Sem email preenchido — mostrar opções
            reply = QMessageBox.information(
                self,
                "Recuperação de Senha",
                "Como você criou sua conta OrdoB?\n\n"
                "• Se criou com Google: use 'Entrar com Google'\n"
                "  e depois defina uma senha no painel OrdoB\n\n"
                "• Se tem email/senha: digite o email acima\n"
                "  e clique em 'Esqueci minha senha' novamente",
                QMessageBox.StandardButton.Ok,
            )
            webbrowser.open("https://ordob.com/login")
            return

        reply = QMessageBox.question(
            self,
            "Enviar Email de Redefinição",
            f"Enviar link de redefinição de senha para:\n{email}\n\n"
            "Se sua conta foi criada com Google,\n"
            "defina uma senha no painel OrdoB após redefinir.\n\n"
            "Após redefinir, volte ao Libryno e faça login.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes,
        )
        if reply == QMessageBox.StandardButton.Yes:
            try:
                import requests
                resp = requests.post(
                    "https://api.ordob.com/api/v1/auth/forgot-password",
                    json={"email": email},
                    timeout=15,
                )
                if resp.status_code == 200:
                    QMessageBox.information(
                        self,
                        "Email Enviado",
                        f"Se o email {email} estiver cadastrado no OrdoB,\n"
                        "você receberá um link de redefinição de senha.\n\n"
                        "Verifique sua caixa de entrada e spam.\n\n"
                        "Após redefinir, volte ao Libryno e faça login."
                    )
                    webbrowser.open("https://ordob.com/login")
                else:
                    QMessageBox.warning(
                        self,
                        "Erro",
                        "Não foi possível enviar o email.\n"
                        "Tente acessar ordob.com/login diretamente."
                    )
            except Exception as e:
                QMessageBox.warning(
                    self,
                    "Erro",
                    f"Erro de conexão: {str(e)[:100]}\n"
                    "Acesse ordob.com/login manualmente."
                )

    def _login_with_ordob(self):
        """Login via navegador (Google OAuth) com callback automático localhost."""
        from src.auth.google_auth import google_auth

        self._set_loading(True)
        self._status_label.setText(t("login.authenticating"))

        class _OAuthWorker(QThread):
            finished = Signal(dict)
            error = Signal(str)

            def run(self):
                ok, token_or_err = google_auth.start_server(timeout=180)
                if not ok or not token_or_err:
                    self.error.emit(token_or_err or "Autenticação cancelada.")
                    return
                user = client.get_user(token_or_err)
                if user:
                    self.finished.emit({"token": token_or_err, "user": user})
                else:
                    self.error.emit("Token recebido, mas inválido no servidor.")

        self._oauth_worker = _OAuthWorker(self)
        self._oauth_worker.finished.connect(self._on_token_success)
        self._oauth_worker.error.connect(self._on_oauth_error)
        self._oauth_worker.start()

    def _on_oauth_error(self, msg: str):
        """OAuth falhou (timeout/cancelado) — oferece fallback manual."""
        self._set_loading(False)
        self._status_label.setText("")

        reply = QMessageBox.question(
            self,
            "Entrar com OrdoB.com",
            f"{msg}\n\n"
            "Deseja inserir um token manualmente?\n"
            "(Ou faça login com email e senha.)",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            self._show_token_dialog()

    def _show_token_dialog(self):
        """Mostra diálogo para colar token do OrdoB."""
        from PySide6.QtWidgets import QInputDialog

        token, ok = QInputDialog.getText(
            self,
            "Colar Token OrdoB",
            "Cole seu token de API do OrdoB:\n\n"
            "Para encontrar seu token:\n"
            "1. Acesse ordob.com/app/profile\n"
            "2. Faça login com email/Google\n"
            "3. Copie o token da seção de Token da API\n"
            "4. Cole aqui",
            QLineEdit.Normal,
        )
        if ok and token.strip():
            self._validate_and_login_token(token.strip())

    def _validate_and_login_token(self, token: str):
        """Valida token do OrdoB e faz login."""
        self._set_loading(True)

        class _TokenWorker(QThread):
            finished = Signal(dict)
            error = Signal(str)

            def __init__(self, tok):
                super().__init__()
                self.tok = tok

            def run(self):
                try:
                    user = client.get_user(self.tok)
                    if user:
                        self.finished.emit({"token": self.tok, "user": user})
                    else:
                        self.error.emit("Token inválido ou expirado.")
                except Exception as e:
                    self.error.emit(f"Erro: {str(e)[:100]}")

        self._token_worker = _TokenWorker(token)
        self._token_worker.finished.connect(self._on_token_success)
        self._token_worker.error.connect(self._on_token_error)
        self._token_worker.start()

    def _on_token_success(self, result: dict):
        """Token validado com sucesso."""
        self._set_loading(False)
        session.login(result["token"], result["user"])
        check_existing_license()
        self._status_label.setText(t("login.success"))
        self._status_label.setStyleSheet(
            "font-size: 12px; color: #44ff44; background: transparent;"
        )
        QMessageBox.information(self, t("messages.success"), t("login.success"))
        self.close()
        if self.on_success:
            self.on_success()

    def _on_token_error(self, msg: str):
        """Token inválido."""
        self._set_loading(False)
        QMessageBox.critical(
            self,
            t("messages.error"),
            f"{msg}\n\n"
            "Verifique se copiou o token completo.\n"
            "Ou faça login com email/senha."
        )

    def closeEvent(self, event):
        if not session.is_authenticated:
            reply = QMessageBox.question(
                self,
                t("login.exit_title"),
                t("login.exit_confirm"),
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )
            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
