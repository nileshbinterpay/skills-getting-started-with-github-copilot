import pytest
from fastapi.testclient import TestClient
import sys
import os

# Ensure src is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import app

@pytest.fixture
def client():
    # Reset activities before each test
    app.activities = {
        "Chess Club": {
            "description": "Sharpen your mind with weekly chess matches.",
            "schedule": "Fridays 3:30-5pm",
            "max_participants": 20,
            "participants": [],
        },
        "Robotics": {
            "description": "Build and program robots for competitions.",
            "schedule": "Wednesdays 4-6pm",
            "max_participants": 15,
            "participants": [],
        },
    }
    with TestClient(app.app) as c:
        yield c
