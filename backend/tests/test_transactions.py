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

def test_add_transaction():
    new_tx = {"id": 3, "amount": 200.0, "status": "success"}
    response = client.post("/transactions", json=new_tx)
    assert response.status_code == 200
    data = response.json()
    assert data["transaction"]["id"] == 3
    assert data["transaction"]["amount"] == 200.0
    assert data["transaction"]["status"] == "success"
    # Verificar que ahora aparece en la lista
    response_get = client.get("/transactions")
    assert any(tx["id"] == 3 for tx in response_get.json()["transactions"])
