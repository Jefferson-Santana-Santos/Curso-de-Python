# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.05
novo_preco = preco - desconto

print("O preço original era R$ {:.2f}. Com 5% de desconto, o novo preço é R$ {:.2f}.".format(preco, novo_preco))
