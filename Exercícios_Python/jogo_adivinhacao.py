#Joguinho de adivinhação


from random import randint
from time import sleep

numero = randint(1,10)
print("Vou pensar em um numero entre 1 e 10... tente adivinhar ! ")
jogador = int(input("Digite um número: "))
print("Pensando...")
sleep(3)
print("Número sorteado:  {} " .format(numero))

if jogador == numero:
    print("Você acertou !")
else:
    print("Você errou ! ")

