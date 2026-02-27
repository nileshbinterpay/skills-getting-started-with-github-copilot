import pytest

# Arrange-Act-Assert pattern is used in all tests

def test_get_activities(client):
    # Arrange: client fixture provides a clean app
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Robotics" in data
    assert data["Chess Club"]["participants"] == []

def test_root_redirects(client):
    # Arrange
    # Act
    response = client.get("/", allow_redirects=False)
    # Assert
    assert response.status_code in (302, 307)
    assert "/static/index.html" in response.headers["location"]
