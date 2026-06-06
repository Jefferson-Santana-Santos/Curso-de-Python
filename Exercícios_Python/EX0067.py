#67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


while True:
    numero = int(input("Quer ver a tabuada de qual valor? "))
    if numero <= -1:
        print("Programa encerrado !")
        break
    for opcao in  range (1,11):
        resultado = opcao*numero
        print(" {} x {} =\033[0:32m {} \033[0m".format(numero,opcao,resultado))





