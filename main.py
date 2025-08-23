from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um smartphone de última geração",
        "preco": 999.99
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um notebook potente para trabalho e jogos",
        "preco": 4999.99
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Um tablet leve e portátil",
        "preco": 2999.99
    }
]


@app.get("/") # Request
def read_root(): #  Response
    return {"Hello": "People"}

@app.get("/produtos")
def listar_produtos():
    return produtos