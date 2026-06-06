#Crie um programa que leia o nome completo de uma pessoa e mostre:
# o  nome com todas as letras maiúsculas
# o nome com todas minúsculas
# Quantas letras ao (todo sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input("Digite seu nome: ")
print("seu nome é {} ".format(nome.upper()))

nom2 = input("Digite seu nome: ")
print("seu nome é {} ".format(nom2.lower()))


# Programa que analisa o nome

nome = input("Digite seu nome completo: ").strip()

# Quantidade de letras sem espaços
total_letras = len(nome.replace(" ", ""))

# Primeiro nome
primeiro_nome = nome.split()[0]
letras_primeiro = len(primeiro_nome)

print("Seu nome completo tem {} letras (sem espaços).".format(total_letras))
print("O primeiro nome '{}' tem {} letras.".format(primeiro_nome, letras_primeiro))
