# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

# Considere US$ 1,00 = R$ 3,27

saldo = 0
cotacao = 3.27
valor = float(input("Insira o valor para depositar em reais : "))
saldo += valor
dolar = (valor / cotacao)
print("Seu saldo é de R$ {:.2f} e você pode comprar {:.2f} dolares".format(saldo,dolar))



