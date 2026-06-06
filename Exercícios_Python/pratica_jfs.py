#Atividade da faculdade Unicid

#Jefferson Santana dos Santos  - experiência prática II


m = -1
estoque = {}   # dicionário para armazenar produtos, quantidades e preços

while m != 0:
    m = int(input("{:=^40}".format("==== Estoque ====") + """
    [0] Sair   
    [1] Registrar um novo produto
    [2] Visualizar estoque
    [3] Entrada de produtos
    [4] Saída de produtos
    Digite uma opção: """))

    if m == 1:
        nome = input("Digite o nome do produto: ").upper()
        qtd = int(input("Digite a quantidade: "))
        preco = float(input("Digite o valor do produto R$: "))
        estoque[nome] = {"quantidade": qtd, "preco": preco}
        print("Produto {} cadastrado com sucesso!".format(nome))

    elif m == 2:
        print("{:=^40}".format("Estoque Atual"))
        if not estoque:
            print("Nenhum produto cadastrado.")
        else:
            for produto, dados in estoque.items():
                print("Produto: {} | Quantidade: {} | Preço: R$ {:.2f}".format(
                    produto, dados["quantidade"], dados["preco"]
                ))

    elif m == 3:  # entrada de produtos
        nome = input("Digite o nome do produto para entrada: ").upper()
        if nome in estoque:
            qtd = int(input("Digite a quantidade a adicionar: "))
            estoque[nome]["quantidade"] += qtd
            print("Entrada registrada! Novo estoque de {}: {}".format(nome, estoque[nome]["quantidade"]))
        else:
            print("Produto não encontrado!")

    elif m == 4:  # saída de produtos
        nome = input("Digite o nome do produto para saída: ").upper()
        if nome in estoque:
            qtd = int(input("Digite a quantidade a retirar: "))
            if qtd <= estoque[nome]["quantidade"]:
                estoque[nome]["quantidade"] -= qtd
                print("Saída registrada! Novo estoque de {}: {}".format(nome, estoque[nome]["quantidade"]))
            else:
                print("Quantidade insuficiente em estoque!")
        else:
            print("Produto não encontrado!")

print("Obrigado por utilizar nossos serviços!")


