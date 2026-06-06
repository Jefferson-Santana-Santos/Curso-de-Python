#Faça um programa que leia dois números  inteiros e compare-os , mostrando na tela
#uma mensagem:
from time import sleep
from colorama import Fore,Style

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print("Comparando números...")
sleep(2)

if numero1 > numero2:
    print(Fore.CYAN + "O Maior número é {}  !".format(numero1))
elif numero1 < numero2:
    print(Fore.GREEN + "O Maior número é {} !".format(numero2))
elif numero1 == numero2:
    print( "Não existe valor" + Fore.LIGHTMAGENTA_EX  + " Maior " +  Style.RESET_ALL + ",os dois são iguais !")
