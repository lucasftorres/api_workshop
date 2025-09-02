from fastapi import FastAPI
from .schema import ProdutoSchema  # Importa a classe ProdutoSchema do módulo schema
from .router import router  # Importa o objeto 'router' do módulo 'router' local.
from typing import List

app = FastAPI()  # Cria uma instância do aplicativo FastAPI.
# 'app' é a instância central do seu aplicativo web.

app.include_router(router)  # Anexa o roteador 'router' ao aplicativo FastAPI.
# Isso registra todas as rotas e operações definidas em 'router' no aplicativo.