import pytest

# Arrange-Act-Assert pattern is used in all tests

def test_signup_success(client):
    # Arrange
    email = "student1@mergington.edu"
    activity = "Chess Club"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]

def test_signup_activity_not_found(client):
    # Arrange
    email = "student2@mergington.edu"
    activity = "Nonexistent Club"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

def test_signup_already_signed_up(client):
    # Arrange
    email = "student3@mergington.edu"
    activity = "Robotics"
    # Act
    first = client.post(f"/activities/{activity}/signup?email={email}")
    second = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert first.status_code == 200
    assert second.status_code == 400
    assert second.json()["detail"] == "Student is already signed up"
