# Programa para calcular o fatorial de um número

numero = int(input("Digite um número: "))

fatorial = 1
sequencia = ""

for i in range(numero, 0, -1):
    fatorial *= i
    if i == 1:
        sequencia += "{}".format(i)
    else:
        sequencia += "{} x ".format(i)

print("{}! = {} = {}".format(numero, sequencia, fatorial))
