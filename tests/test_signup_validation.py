from fastapi.testclient import TestClient

from src.app import app


def test_duplicate_signup_is_rejected():
    client = TestClient(app)

    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Student is already signed up"}
