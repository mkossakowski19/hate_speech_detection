from typing import Dict

import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture(scope="module")
def input_data() -> Dict[str, str]:
    return {"text": "Musimy wygrać ten mecz! Do boju Polsko!"}


client = TestClient(app)


def test_sample_endpoint(input_data: Dict[str, str]):
    response = client.post("/detect-hate-speech", json=input_data)

    assert response.status_code == 200
    assert set(response.json().keys()) == {"predicted_class"}
    assert isinstance(response.json()["predicted_class"], str)
