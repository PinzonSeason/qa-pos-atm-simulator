from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "POS + ATM simulator is alive!"}
