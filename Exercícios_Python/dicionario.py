
estoque = {}


qtd = 123
prc = 111


estoque["Arroz"] = {"quantidade": 10, "preco": 5.50}
estoque["Feijao"] = {"quantidade": 8, "preco": 7.20}
estoque["Macarrao"] = {"quantidade": 15, "preco": 4.00}



for nome_produto, atributos in estoque.items():
    print(nome_produto, "→ Quantidade:", atributos["quantidade"], "| Preço:", atributos["preco"])
