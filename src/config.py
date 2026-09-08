"""Configurações centralizadas do LIBRYNO."""
import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

from dotenv import load_dotenv

IS_FROZEN = getattr(sys, "frozen", False)

if IS_FROZEN:
    BASE_DIR = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
    _DATA_ROOT = Path(os.environ.get("APPDATA") or (Path.home() / ".config")) / "Libryno"
else:
    BASE_DIR = Path(__file__).resolve().parent.parent
    _DATA_ROOT = BASE_DIR

ENV_FILE = BASE_DIR / ".env"

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
else:
    load_dotenv(BASE_DIR / ".env.example")

DATA_DIR = _DATA_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


class Config:
    APP_NAME = "LIBRYNO"
    APP_VERSION = os.getenv("APP_VERSION", "2.0.0")
    APP_DEBUG = os.getenv("APP_DEBUG", "false").lower() == "true"

    # Versionamento e Auto-updater
    UPDATE_CHECK_URL = os.getenv("UPDATE_CHECK_URL", "https://api.github.com/repos/ordo-b/LIBRYNO/releases/latest")
    UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "stable")  # stable, beta, alpha
    AUTO_UPDATE_ENABLED = os.getenv("AUTO_UPDATE_ENABLED", "true").lower() == "true"
    UPDATE_CHECK_INTERVAL_HOURS = int(os.getenv("UPDATE_CHECK_INTERVAL_HOURS", "24"))

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{DATA_DIR / 'libryno.db'}",
    )

    ORDOB_API_URL = os.getenv("ORDOB_API_URL", "https://api.ordob.com/api")
    ORDOB_API_URL_DEV = os.getenv("ORDOB_API_URL_DEV", "http://localhost:8000/api")
    ORDOB_PRODUCT_SLUG = os.getenv("ORDOB_PRODUCT_SLUG", "libryno")
    ORDOB_ENV = os.getenv("ORDOB_ENV", "production")

    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "libryno://auth/callback")

    SYNC_ENABLED = os.getenv("SYNC_ENABLED", "true").lower() == "true"
    SYNC_INTERVAL = int(os.getenv("SYNC_INTERVAL", "300"))  # 5 minutos

    @classmethod
    def get_api_url(cls) -> str:
        if cls.APP_DEBUG:
            return cls.ORDOB_API_URL_DEV
        return cls.ORDOB_API_URL

    @staticmethod
    def resource_path(relative: str) -> str:
        """Resolve caminho de recurso (funciona em dev e empacotado)."""
        base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
        return str(base / relative)

    @classmethod
    def get_current_version(cls) -> tuple:
        """Retorna versão atual como tupla (major, minor, patch) para comparação."""
        version_str = cls.APP_VERSION
        # Remove prefixos como 'v' se existirem
        version_str = version_str.lstrip('v')
        parts = version_str.split('.')
        # Garante que tenha 3 partes
        while len(parts) < 3:
            parts.append('0')
        return tuple(int(p) for p in parts[:3])

    @classmethod
    def is_newer_version(cls, remote_version: str) -> bool:
        """Compara versão remota com a atual. Retorna True se remota for mais nova."""
        try:
            remote = tuple(int(p) for p in remote_version.lstrip('v').split('.')[:3])
            local = cls.get_current_version()
            return remote > local
        except (ValueError, IndexError):
            return False

    @classmethod
    def get_update_info(cls) -> dict:
        """Busca informações da última release no GitHub."""
        if not cls.AUTO_UPDATE_ENABLED:
            return {"update_available": False, "reason": "auto_update_disabled"}

        try:
            req = urllib.request.Request(
                cls.UPDATE_CHECK_URL,
                headers={
                    "Accept": "application/vnd.github.v3+json",
                    "User-Agent": f"{cls.APP_NAME}/{cls.APP_VERSION}",
                },
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())

            tag_name = data.get("tag_name", "").lstrip('v')
            download_urls = {
                "windows": None,
                "linux_deb": None,
                "linux_appimage": None,
            }

            for asset in data.get("assets", []):
                name = asset.get("name", "").lower()
                if name.endswith(".exe") and "setup" in name:
                    download_urls["windows"] = asset["browser_download_url"]
                elif name.endswith(".deb"):
                    download_urls["linux_deb"] = asset["browser_download_url"]
                elif name.endswith(".appimage"):
                    download_urls["linux_appimage"] = asset["browser_download_url"]

            current_version = cls.get_current_version()
            remote_version = tuple(int(p) for p in tag_name.split('.')[:3])

            return {
                "update_available": remote_version > current_version,
                "current_version": ".".join(str(p) for p in current_version),
                "latest_version": tag_name,
                "release_notes": data.get("body", ""),
                "published_at": data.get("published_at"),
                "download_urls": download_urls,
                "html_url": data.get("html_url"),
            }

        except urllib.error.URLError as e:
            return {"update_available": False, "reason": f"network_error: {e}"}
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            return {"update_available": False, "reason": f"parse_error: {e}"}
        except Exception as e:
            return {"update_available": False, "reason": f"unexpected_error: {e}"}
