from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)

def test_average_rating():
    # Test case 1: valid comic rating
    response = client.get("/api/comics/1/rating/")
    assert response.status_code == 200

    # Test case 2: unexisting comic
    response = client.get("/api/comics/10000/rating/")
    assert response.status_code == 400
    assert response.json() == {"detail": "Bad Request"}
