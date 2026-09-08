"""Autenticação Google OAuth para desktop via servidor local.

Fluxo:
1. Servidor local escuta em porta aleatória (localhost).
2. Abre no navegador: api.ordob.com/api/v1/auth/google?callback=http://localhost:PORTA
3. Usuário autentica com Google; a API redireciona para o servidor local.
4. O token chega automaticamente — sem copiar/colar nada.

Fallback: login por email/senha ou token manual seguem disponíveis na tela de login.
"""
import threading
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from src.config import Config
from src.utils.logger import logger


class _OAuthCallbackHandler(BaseHTTPRequestHandler):
    """Handler para capturar callback do OAuth."""

    token_received = None  # threading.Event
    received_token = None  # list para armazenar token

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        if "token" in params:
            _OAuthCallbackHandler.received_token[0] = params["token"][0]
            _OAuthCallbackHandler.token_received.set()
            self._respond_ok("✅ Autenticado! Voltando ao Libryno...")
        elif "error" in params:
            _OAuthCallbackHandler.received_token[0] = ""
            _OAuthCallbackHandler.token_received.set()
            self._respond_error("Autenticação falhou. Tente novamente.")
        else:
            self._respond_error("Parâmetro 'token' não encontrado na URL.")

    def _respond_ok(self, message: str):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Libryno - Autenticado</title>
<style>
body {{ background: #1a1a2e; color: #5CE1E6; font-family: sans-serif;
       display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
.box {{ text-align: center; padding: 40px; }}
h1 {{ font-size: 48px; }}
p {{ font-size: 18px; color: #a0a0a0; }}
</style></head>
<body><div class="box"><h1>✅</h1><p>{message}</p></div></body></html>"""
        self.wfile.write(html.encode("utf-8"))

    def _respond_error(self, message: str):
        self.send_response(400)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Libryno - Erro</title>
<style>
body {{ background: #1a1a2e; color: #ff4444; font-family: sans-serif;
       display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
.box {{ text-align: center; padding: 40px; }}
</style></head>
<body><div class="box"><h1>❌</h1><p>{message}</p></div></body></html>"""
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        pass  # Silenciar logs HTTP


class GoogleOAuthManager:
    """Gerencia fluxo Google OAuth para desktop."""

    def __init__(self):
        self._server = None
        self._thread = None
        self._port = None
        self._stop_event = threading.Event()

    def start_server(self, timeout: int = 120) -> tuple[bool, str]:
        """Inicia servidor local e abre Google OAuth no navegador.

        Retorna (sucesso, token_ou_erro). Em caso de sucesso, o segundo
        elemento é o token; em falha, uma mensagem de erro.
        """
        import socket

        # Encontrar porta disponível
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", 0))
        self._port = sock.getsockname()[1]
        sock.close()

        # Configurar estado do handler
        _OAuthCallbackHandler.token_received = threading.Event()
        _OAuthCallbackHandler.received_token = [None]

        # Criar servidor
        self._server = HTTPServer(("localhost", self._port), _OAuthCallbackHandler)
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

        logger.info("OAuth server started on port {}", self._port)

        # Abrir OAuth via OrdoB com callback localhost
        auth_url = (
            f"{Config.ORDOB_API_URL}/v1/auth/google"
            f"?callback=http://localhost:{self._port}"
        )
        webbrowser.open(auth_url)

        # Esperar token ou timeout
        _OAuthCallbackHandler.token_received.wait(timeout=timeout)

        # Parar servidor
        self._server.shutdown()
        self._server.server_close()

        token = _OAuthCallbackHandler.received_token[0]
        if token:
            logger.info("OAuth token received")
            return True, token
        logger.warning("OAuth timeout - no token received")
        return False, "Tempo esgotado. Tente novamente."

    def get_auth_url(self) -> str:
        """Retorna URL de autenticação Google via OrdoB."""
        return f"{Config.ORDOB_API_URL}/v1/auth/google"

    def get_login_url(self) -> str:
        """Retorna URL de login OrdoB."""
        return "https://ordob.com/login"

    def get_cadastro_url(self) -> str:
        """Retorna URL de cadastro OrdoB."""
        return "https://ordob.com/cadastro"


# Instância global
google_auth = GoogleOAuthManager()
