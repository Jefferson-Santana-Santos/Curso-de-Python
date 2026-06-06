#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.


soma = 0
for i in range(1, 7):
    n1 = int(input("Digite um numero {} : ".format(i)))
    if n1 % 2 == 0:
        soma = soma + n1
    elif n1 % 2 != 0:
        print("Resultado inválido,\033[1:31m digite novamete.\033[0m O número digitado é \033[1:31m ÍMPAR \033[0m!")

print(" O resultado é:\033[1:32m {} \033[0m de \033[1:35m {} \033[0m repetições!".format(soma,i))



