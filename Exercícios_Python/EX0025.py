#crie um programa que leia o primeiro e o ultimo nome digitados

nome = str(input("qual seu nome completo ")).strip()
nome = nome.split()
print( "Olá, seu primeiro nome é {} "  .format(nome[0],))
print("Seu ultimo nome é {} " .format(nome[len(nome)-1]))