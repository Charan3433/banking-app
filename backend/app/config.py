import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BASE_DIR.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
load_dotenv(PROJECT_ROOT / ".env")


def _resolve_database_uri() -> str:
    configured_uri = os.getenv("DATABASE_URL")
    if configured_uri:
        if configured_uri.startswith("sqlite:///") and not configured_uri.startswith("sqlite:////"):
            raw_path = configured_uri[len("sqlite:///"):]
            if raw_path.startswith("/"):
                db_path = Path(raw_path)
            else:
                db_path = PROJECT_ROOT / raw_path
            db_path = db_path.resolve()
            db_path.parent.mkdir(parents=True, exist_ok=True)
            return f"sqlite:///{db_path}"
        return configured_uri
    return f"sqlite:///{(DATA_DIR / 'banking.db').resolve()}"


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "banking-dev-secret")
    SQLALCHEMY_DATABASE_URI = _resolve_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", "8"))
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
