#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

numero = int(input("Digite o número da tabuada: "))

print("Tabuada do número: {} ".format(numero))
for i in range(1, 11):
    print("{} x {} =\033[1:32m  {} \033[0m".format(numero, i, numero * i))
