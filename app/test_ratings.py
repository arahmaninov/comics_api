from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)

def test_rating():
    # Test case 1: valid data, new user rating
    response = client.post("/api/ratings/?comic_id=1&user_id=10&value=5")
    assert response.status_code == 200
    assert response.json() == {"addition": "ok"}

    # Test case 2: valid data, updating existing user rating
    response = client.post("/api/ratings/?comic_id=1&user_id=1&value=3")
    assert response.status_code == 200
    assert response.json() == {"addition": "ok"}

    # Test case 3: wrong data, unexisting comic_id
    response = client.post("/api/ratings/?comic_id=10000&user_id=1&value=5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Bad Request"}
    
    # Test case 4: wrong data, rating value is out of range 1...5
    response = client.post("/api/ratings/?comic_id=1&user_id=1&value=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Bad Request"}
