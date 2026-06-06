#Faça um progragama que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai  se alistar ao serviço militar.
# se é a hora de se alistar.
# se já passou do tempo do alistamento.
# seu programa  também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
from colorama import Fore,Style

ano_nascimento = int(input("Olá, digite o ano de nascimento : "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade < 18:
    saldo = 18 - idade
    print("Ainda não está na hora de se Alistar.Você tem {} anos. ".format(idade))
    print("Ainda faltam {} anos.".format(saldo))

elif idade == 18:
    print("está na hora de se Alistar !! ")

elif idade > 18:
    saldo = idade - 18
    print(Fore.RED + "Você excedeu o prazo em {} anos para o Alistamento militar.".format(saldo) + Style.RESET_ALL + " Compareça imediatamente !")

