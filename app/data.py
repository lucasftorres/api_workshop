from typing import List, Dict


class Produtos:
    produtos: List[Dict[str, any]] = [
        {
            "id": 1,
            "nome": "Smartphone",
            "descricao": "Um smartphone de última geração",
            "preco": 999
        },
        {
            "id": 2,
            "nome": "Notebook",
            "descricao": "Um notebook potente para trabalho e jogos",
            "preco": 4999
        },
        {
            "id": 3,
            "nome": "Tablet",
            "descricao": "Um tablet leve e portátil",
            "preco": 2999
        }
    ]

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id: int):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404, "Mensagem": "Produto não encontrado"}

    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        return produto