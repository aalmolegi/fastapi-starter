from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_login_crud():
    # register
    r = client.post("/api/users", json={"email": "a@b.com", "password": "secret123"})
    assert r.status_code == 201

    # login (OAuth2PasswordRequestForm expects form data)
    r = client.post("/api/auth/login", data={"username": "a@b.com", "password": "secret123"})
    assert r.status_code == 200
    token = r.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # create item
    r = client.post("/api/items", json={"title": "First", "description": "Desc"}, headers=headers)
    assert r.status_code == 201
    item_id = r.json()["id"]

    # list items
    r = client.get("/api/items", headers=headers)
    assert r.status_code == 200
    assert len(r.json()) >= 1

    # update item
    r = client.patch(f"/api/items/{item_id}", json={"title": "Updated"}, headers=headers)
    assert r.status_code == 200
    assert r.json()["title"] == "Updated"

    # delete item
    r = client.delete(f"/api/items/{item_id}", headers=headers)
    assert r.status_code == 204
