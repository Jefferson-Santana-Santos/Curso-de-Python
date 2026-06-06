# GAME: Pedra Papel e Tesoura

import random
from time import sleep

print("{:^40}".format("JOKENPÔ"))
opcao_jogador = int(input("""
 [0] Pedra 
 [1] Papel 
 [2] Tesoura 
 Escolha uma opção: """))
print("-=-="*10)

item = ("\033[1:32:40m Pedra \033[0m ", "\033[1:33:40m Papel \033[0m ", "\033[1:34:40m Tesoura \033[0m ")

computador = random.randint(0, 2)

print("Jo-",end="")
sleep(0.5)
print("KENNN",end="")
sleep(0.5)
print("-PÔ!! ",end="")
sleep(0.5)

resultado = ""  # variável para guardar o resultado

if computador == 0:
    if opcao_jogador == 0:
        resultado = "EMPATOU"
    elif opcao_jogador == 1:
        resultado = "VENCEU"
    elif opcao_jogador == 2:
        resultado = "PERDEU"
    else:
        resultado = "INVÁLIDO"

elif computador == 1:
    if opcao_jogador == 0:
        resultado = "PERDEU"
    elif opcao_jogador == 1:
        resultado = "EMPATOU"
    elif opcao_jogador == 2:
        resultado = "VENCEU"
    else:
        resultado = "INVÁLIDO"

elif computador == 2:
    if opcao_jogador == 0:
        resultado = "VENCEU"
    elif opcao_jogador == 1:
        resultado = "PERDEU"
    elif opcao_jogador == 2:
        resultado = "EMPATOU"
    else:
        resultado = "INVÁLIDO"

# Mensagem final única
print("Jogador - {} x {} - Máquina | Você: \033[1:32:40m {} \033[0m ".format(item[opcao_jogador], item[computador], resultado))
