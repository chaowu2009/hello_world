import pytest
from app import *

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_root(client):
    res = client.get('/')
    assert b'Hello world!' in res.data
