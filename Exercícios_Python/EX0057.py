"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
peça a digitação novamente até ter um valor correto."""


sexo = str(input("Digite o sexo (M/F): ")).upper().strip()[0]
while sexo != "M" and sexo != "F":
        print("Digite um valor \033[1:31mVálido! \033[0m")
        sexo = str(input("Digite o sexo (M/F): ")).upper().strip()[0]

if sexo == "M".upper():
    sexo = "Masculino"
elif sexo == "F".upper():
    sexo = "Feminino"

print("Sexo \033[1:32m {} \033[0m Registrado com sucesso ! ".format(sexo))



