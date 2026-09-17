import pytest
from app import crear_app


@pytest.fixture
def app(tmp_path):
    db_path = tmp_path / "test.db"
    app = crear_app(str(db_path))
    app.config.update(TESTING=True)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def token(client):
    client.post("/registro", json={"username": "ana", "password": "1234"})
    respuesta = client.post("/login", json={"username": "ana", "password": "1234"})
    return respuesta.get_json()["token"]

@pytest.fixture
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}