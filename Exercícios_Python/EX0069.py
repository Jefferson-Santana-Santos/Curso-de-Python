# 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:


# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

from datetime import date
ano = date.today().year

contagem_m = 0
contagem_f = idade_geral = idade_feminino = 0

while True:

    print("{:^30}".format("===== \033[1:32m  Cadastre uma pessoa \033[0m ======="))
    sexo = str(input("Qual o sexo? [M/F]: ")).strip().upper()[0]
    idade = int(input("Qual a idade? : "))

    if sexo == "M":
        contagem_m += 1
    if idade >= 18:
        idade_geral += 1
    else:
        idade_feminino += 1

    print("============" * 3)

    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        print("A quantidade de pessoas maior de 18 anos é {}. ".format(idade_geral))
        print("Foram cadastrados {} {}. E temos {} Mulheres abaixo de 20 anos."
              .format(contagem_m, "Homem" if contagem_m == 1 else "Homens", idade_feminino))
        break



