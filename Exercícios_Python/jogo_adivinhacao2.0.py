#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. ]
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from time import sleep
from random import randint



resposta = input(str("""Olá !! 
Sou o \033[0:32m Adivinhation 2.0 , \033[0m você é bom em palpites? \033[0:35m S/N \033[0m: """)).strip().upper()[:1]
sleep(0.5)

if resposta == "S":
    print("Maravilha ! eu sabia disso... ")
else:
    print("Hmmm... eu acho que você consegue!")

sleep(0.4)
tentativa = 0
computador = randint(0, 10)
jogador = -1

while jogador != computador:

    jogador = int(input(" Digite um número entre \033[0:35m 0 a 10 \033[0m e tente adivinhar! \n "))
    tentativa += 1
    print("Tentativa Nº {}".format(tentativa))

    if jogador == computador:
        print("Sua jogada {} ".format(jogador))
        print("Você \033[0:32m  acertou! \033[0m o número correto é: \033[0:32m  {} \033[0m ".format(computador))
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[:1]
        if continuar == "S":
            jogador = -1
            computador = randint(0, 10)
        else:
            print("Hmmm... Ok, Até a próxima!!")

    elif jogador != computador:
        print("Você \033[0:31m errou! \033[0m \033[0:35m tente novamente! \033[0m ".format(computador))




















