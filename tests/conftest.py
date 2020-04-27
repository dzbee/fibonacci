import pytest

from app import app

@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    return app

@pytest.fixture
def test_client(test_app):
    return test_app.test_client()
