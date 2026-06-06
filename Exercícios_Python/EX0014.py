#crie um programa que leia um número real qualquer pelo teclado e mostre na tela  a sua porção inteira.

import math

# Leia um número real
numero = float(input("Digite um número real: "))

# Porção inteira
inteiro = math.trunc(numero)

print("O número digitado foi {} e sua porção inteira é {}".format(numero, inteiro))
