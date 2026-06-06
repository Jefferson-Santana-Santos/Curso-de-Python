#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM

# Até 14 anos: INFANTIL

# Até 19 anos: JÚNIOR

# Até 25 anos: SÊNIOR

# Acima de 25 anos: MASTER

from datetime import date
from colorama import Fore

ano_nascimento = int(input("Digite o ano de nascimento do Atleta: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print("você tem {} anos. ".format(idade) + "Sua categoria de Atleta é" + Fore.GREEN +  " MIRIM ")

elif idade <= 14:
    print("você tem {} anos. ".format(idade) + "Sua categoria de Atleta é" + Fore.LIGHTMAGENTA_EX +  " INFANTIL ")

elif idade <= 19:
    print("você tem {} anos. ".format(idade) + "Sua categoria de Atleta é" + Fore.CYAN +  " JÚNIOR ")

elif idade <= 25:
    print("você tem {} anos. ".format(idade) + "Sua categoria de Atleta é" + Fore.MAGENTA +  " SÊNIOR ")

else:
    print("você tem {} anos. ".format(idade) + "Sua categoria de Atleta é" + Fore.BLUE + " MASTER ")


