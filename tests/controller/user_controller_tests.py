import pytest
from flask import Flask, jsonify
from controllers.user_controller import user_blueprint
from model import User

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user_success(client):
    # Prepare test data
    user_data = {
        "name": "Elly Tal",
        "email": "elly@tal.com",
        "phone": "122334"
    }

    # Send POST request to the /create endpoint
    response = client.post('/create', json=user_data)

    # Assert the response
    assert response.status_code == 200
    data = response.get_json()
    assert "id" in data
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]