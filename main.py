from fastapi import FastAPI

app = FastAPI()
@app.get("/status")
def status():
    return {"status": "Oscar is functioning perfectly."}

@app.get("/")
def read_root():
    return {"message": "Oscar is online. 🐉"}

