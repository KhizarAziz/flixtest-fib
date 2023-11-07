from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():

    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == 1

    response = client.get("/3")
    assert response.status_code == 200
    assert response.json() == 2

    response = client.get("/7")
    assert response.status_code == 200
    assert response.json() == 13
