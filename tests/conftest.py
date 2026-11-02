import pytest

from app import create_app, db
from app.models import Character, Sex


@pytest.fixture
def app(tmp_path):
    class TestConfig:
        TESTING = True
        SECRET_KEY = "test"
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{tmp_path / 'test.db'}"
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        UPLOAD_FOLDER = str(tmp_path / "uploads")
        WTF_CSRF_ENABLED = False

    application = create_app(TestConfig)
    yield application

    with application.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def sample_character(app):
    with app.app_context():
        character = Character(
            name="Aino",
            description="A quiet wanderer from the northern woods.",
            sex=Sex.female,
        )
        db.session.add(character)
        db.session.commit()
        return character.id
