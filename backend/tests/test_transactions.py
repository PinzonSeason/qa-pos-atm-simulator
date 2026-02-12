from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_transactions():
    response = client.get("/transactions")
    assert response.status_code == 200
    data = response.json()
    assert "transactions" in data
    assert isinstance(data["transactions"], list)
    assert len(data["transactions"]) > 0
