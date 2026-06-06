total = 0
menor_valor = 0
maior_valor = 0
nome_produto = ""

while True:
    print(f"{'=========== Super Loja Santana ===========':^40}")
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço R$: "))
    total += preco

    # se for o primeiro produto, inicializa o menor_valor
    if menor_valor == 0 or preco < menor_valor:
        menor_valor = preco
        nome_produto = produto

    # conta produtos acima de 1000
    if preco > 1000:
        maior_valor += 1

    continuar = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if continuar == "N":
        print(f"{'=========== Fim da compra ===========':^40}")
        print(f"O total da compra foi de R$: {total:.2f}.")
        print(f"Temos {maior_valor} produtos custando mais de R$ 1000.00.")
        print(f"O produto mais barato foi o {nome_produto} que custa R$ {menor_valor:.2f}")
        break
