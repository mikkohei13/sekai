from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_object=None):
    app = Flask(__name__)

    if config_object is None:
        from app.config import Config

        app.config.from_object(Config)
    else:
        app.config.from_object(config_object)

    upload_folder = Path(app.config["UPLOAD_FOLDER"])
    upload_folder.mkdir(parents=True, exist_ok=True)

    db.init_app(app)

    from app import models  # noqa: F401
    from app.routes import bp

    app.register_blueprint(bp)

    from app.admin import init_admin

    # /admin is intentionally open — local development only.
    init_admin(app)

    with app.app_context():
        db.create_all()

    return app
