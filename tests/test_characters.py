from app import db
from app.models import Character


def test_index_lists_character(client, sample_character):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Aino" in response.data
    assert b"quiet wanderer" in response.data
    assert b"female" in response.data


def test_index_empty(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"No characters yet" in response.data


def test_admin_reachable(client):
    response = client.get("/admin/")
    assert response.status_code == 200


def test_character_persisted(app, sample_character):
    with app.app_context():
        character = db.session.get(Character, sample_character)
        assert character is not None
        assert character.name == "Aino"
        assert character.sex.value == "female"
