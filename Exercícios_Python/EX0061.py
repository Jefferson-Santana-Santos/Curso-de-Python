# Programa que mostra os 10 primeiros termos de uma PA usando while

termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

contador = 1
termo = termo1

while contador <= 10:
    print("{}".format(termo), end=" ")
    termo += razao
    contador += 1

print("Acabou!")
