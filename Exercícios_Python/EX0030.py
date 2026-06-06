#crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
from colorama import Fore, Style


numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(Fore.BLUE + "Esse número é PAR")
else:
    print(Fore.GREEN + "Esse número é ÍMPAR")


