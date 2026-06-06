# Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print("\033[0:30:43m Iniciar a contagem !! \033[0m")
for  c in range (10,-1,-1):
    print(c)
    sleep(1)
print(": \033[0:30:43m Bummmm  !!! \033[0m")



