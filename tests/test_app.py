import pytest
from source.app import app


@pytest.fixture
def client():
    yield app.test_client()


def test_index(client):
    rv = client.get('/')
    assert 200 == rv.status_code
    assert b'Users' in rv.data


def test_user_0(client):
    rv = client.get('/0')
    assert 200 == rv.status_code
    assert b'Jeff Bezos' in rv.data
    assert b'Customer' in rv.data


def test_invalid_user(client):
    rv = client.get('/999999999999')
    assert 404 == rv.status_code


def test_invalid_page(client):
    rv = client.get('/NaN')
    assert 404 == rv.status_code
