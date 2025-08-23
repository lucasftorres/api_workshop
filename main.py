from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Request
def read_root(): #  Response
    return {"Hello": "World"}