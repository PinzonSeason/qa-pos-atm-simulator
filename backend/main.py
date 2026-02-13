from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista simulada de transacciones
transactions = [
    {"id": 1, "amount": 100.0, "status": "success"},
    {"id": 2, "amount": 50.0, "status": "failed"}
]

class Transaction(BaseModel):
    id: int
    amount: float
    status: str

# Endpoint básico de transacciones
@app.get("/transactions")
def get_transactions():
    return {"transactions": transactions}

# Nuevo endpoint para agregar transacciones
@app.post("/transactions")
def add_transaction(transaction: Transaction):
    transactions.append(transaction.dict())
    return {"message": "Transaction added successfully", "transaction": transaction}
