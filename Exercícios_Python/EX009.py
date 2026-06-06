# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite o número da tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
