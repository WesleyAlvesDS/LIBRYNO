"""Gerenciamento de licença premium via OrdoB com verificação de assinatura."""
import threading
import time

from src.auth.ordob_client import client
from src.auth.session import session
from src.config import Config
from src.utils.logger import logger


class LicenseManager:
    """Gerenciador de licença premium com verificação periódica."""

    CHECK_INTERVAL = 3600

    def __init__(self):
        self._last_check = 0.0
        self._check_thread: threading.Thread | None = None
        self._stop_event = threading.Event()

    def validate_license(self, license_key: str) -> tuple[bool, str]:
        """Valida uma chave de licença OrdoB Premium."""
        result = client.validate_license(license_key)
        if result is None:
            return False, "Não foi possível conectar ao servidor OrdoB."

        if result.get("valid"):
            session.set_premium(True, license_key)
            org = result.get("organization", "")
            role = result.get("role", "owner")
            expires = result.get("expires_at", "Nunca")
            logger.info("License activated: {} for {} (role: {})", license_key, org, role)
            self._last_check = time.time()
            return True, (
                f"Licença OrdoB Premium ativada!\n\n"
                f"Organização: {org}\n"
                f"Perfil: {role}\n"
                f"Expira: {expires}"
            )

        error = result.get("error", "Licença inválida.")
        expires = result.get("expires_at")
        session.set_premium(False)
        logger.warning("License invalid: {} - {}", license_key, error)
        return False, f"{error}\n\nData de expiração: {expires or 'N/A'}"

    def check_existing_license(self) -> bool:
        """Verifica se já existe uma licença salva na sessão."""
        if not session.is_premium and not session.license_key:
            return False

        if session.license_key:
            result = client.validate_license(session.license_key)
            if result and result.get("valid"):
                session.set_premium(True, session.license_key)
                self._last_check = time.time()
                return True
            session.set_premium(False)
            logger.info("Existing license expired or invalid, downgrading to free")

        if session.is_premium:
            return True

        return False

    def validate_session_token(self) -> bool:
        """
        Valida se o token de sessão ainda é válido no servidor OrdoB.
        Retorna True se válido, False se expirado/revogado.
        """
        if not session.token:
            return False

        user_data = client.get_user(session.token)
        if user_data is None:
            logger.warning("Token validation failed — API unreachable")
            return False

        # Atualizar dados do usuário com os mais recentes do servidor
        session._user = user_data
        session._save_session()
        logger.info("Token validated successfully for: {}", session.user_email)
        return True

    def periodic_check_start(self):
        """Inicia verificação periódica de licença em background."""
        if self._check_thread and self._check_thread.is_alive():
            return

        self._stop_event.clear()
        self._check_thread = threading.Thread(
            target=self._periodic_check_loop,
            daemon=True,
            name="LicenseCheck",
        )
        self._check_thread.start()

    def _periodic_check_loop(self):
        """Loop de verificação periódica da licença."""
        while not self._stop_event.is_set():
            try:
                # 1) Validar token de sessão
                if session.token:
                    if not self.validate_session_token():
                        logger.warning(
                            "Session token expired/invalid — logging out"
                        )
                        session.logout()
                        continue

                # 2) Validar licença
                if session.license_key:
                    result = client.validate_license(session.license_key)
                    if result and result.get("valid"):
                        if not session.is_premium:
                            session.set_premium(True, session.license_key)
                            logger.info("License restored via periodic check")
                    else:
                        if session.is_premium:
                            session.set_premium(False)
                            logger.info("License expired, downgraded to free")
                            self._notify_license_expired()
            except Exception as e:
                logger.warning("Periodic license check error: {}", e)

            self._stop_event.wait(self.CHECK_INTERVAL)

    def _notify_license_expired(self):
        """Emite notificação quando a licença expira."""
        try:
            from src.features.notifications import NotificationsCRUD
            NotificationsCRUD.create(
                titulo="Licença expirada",
                mensagem=(
                    "Sua licença OrdoB Premium expirou. "
                    "Renove para continuar usando recursos premium."
                ),
                tipo="license_expired",
            )
        except Exception as e:
            logger.error("Error notifying license expiry: {}", e)

    def periodic_check_stop(self):
        """Para a verificação periódica."""
        self._stop_event.set()
        if self._check_thread and self._check_thread.is_alive():
            self._check_thread.join(timeout=3)
        logger.info("License periodic check stopped")


_license_manager = LicenseManager()


def validate_license(license_key: str) -> tuple[bool, str]:
    """Valida uma chave de licença."""
    return _license_manager.validate_license(license_key)


def check_existing_license() -> bool:
    """Verifica se já existe uma licença salva na sessão."""
    return _license_manager.check_existing_license()


def auto_detect_premium() -> bool:
    """Detecta automaticamente se a conta OrdoB tem licença Premium.
    
    Chamado após login bem-sucedido.
    Consulta a API OrdoB para verificar se existem licenças ativas
    para o produto Libryno. Se encontrar, ativa premium automaticamente.
    """
    if session.is_premium:
        return True  # Já é premium
    
    if not session.token:
        return False
    
    try:
        licenses = client.get_licenses(session.token)
        if not licenses:
            logger.info("No licenses found for user")
            return False
        
        # Procurar licença ativa para o produto libryno
        # A API retorna 'product' como objeto relacionado: {"slug": ..., ...}
        for lic in licenses:
            product = lic.get("product") or {}
            product_slug = product.get("slug", "") if isinstance(product, dict) else str(product)
            status = lic.get("status", "")
            license_key = lic.get("license_key", "") or lic.get("key", "")

            if (product_slug == Config.ORDOB_PRODUCT_SLUG
                    and status in ("active", "trial")
                    and license_key):
                logger.info("Auto-detected active license: {} (status: {})", 
                           license_key[:8] + "...", status)
                session.set_premium(True, license_key)
                return True
        
        logger.info("No active license found for product: {}", Config.ORDOB_PRODUCT_SLUG)
        return False
    except Exception as e:
        logger.warning("Auto-detect premium failed: {}", e)
        return False


def validate_session_token() -> bool:
    """Valida se o token de sessão ainda é válido no servidor."""
    return _license_manager.validate_session_token()


def deactivate_license():
    """Remove a licença premium da sessão."""
    session.set_premium(False)
    _license_manager.periodic_check_stop()
    logger.info("License deactivated")


def get_license_info() -> dict | None:
    """Retorna informações da licença atual."""
    if not session.is_premium or not session.license_key:
        return None
    return {
        "key": session.license_key,
        "status": "active",
        "user": session.user_name,
        "organization": session.user.get("organization_name") if session.user else None,
    }


def start_license_monitoring():
    """Inicia o monitoramento periódico de licença em background."""
    if session.license_key:
        _license_manager.periodic_check_start()


def stop_license_monitoring():
    """Para o monitoramento de licença."""
    _license_manager.periodic_check_stop()
