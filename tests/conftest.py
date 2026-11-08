import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app("test")
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_client(client):
    # register + login a seeker
    client.post("/register", data={"name":"Test Seeker","email":"t@test.com","password":"pass","role":"seeker","location":"Downtown"})
    client.post("/login", data={"email":"t@test.com","password":"pass"})
    return client
