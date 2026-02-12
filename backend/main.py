from fastapi import FastAPI

app = FastAPI()

# Endpoint básico de transacciones
@app.get("/transactions")
def get_transactions():
    # Por ahora, devolveremos datos simulados
    return {
        "transactions": [
            {"id": 1, "amount": 100.0, "status": "success"},
            {"id": 2, "amount": 50.0, "status": "failed"}
        ]
    }
