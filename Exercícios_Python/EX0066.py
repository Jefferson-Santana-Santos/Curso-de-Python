#Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


numero = 0
contador = -1
soma = 0

while True:
    numero = int(input("Digite um número (P/ Sair: 999): "))
    contador += 1
    if numero == 999:
        break
    soma = soma + numero

print (" Você digitou {} números. A soma dos valores é {}.".format(contador, soma))

