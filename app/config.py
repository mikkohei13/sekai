import os
from pathlib import Path


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql+psycopg2://sekai:sekai@localhost:5432/sekai",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    _default_uploads = Path(__file__).resolve().parent / "static" / "uploads"
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", str(_default_uploads))
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8 MB
