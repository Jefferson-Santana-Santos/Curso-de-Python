#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today()

menor = 0
maior = 0

for c in range(1,8):
    idade = int(input("Digite o ano de nascimento da {}º Pessoa: ".format(c)))
    calculo_idade = ano_atual.year - idade

    if calculo_idade < 18:
        menor = menor + 1
    else:
        maior = maior + 1

print(" {}  são Menor de idade !".format(menor))
print(" {}  são Maior de idade !".format(maior))