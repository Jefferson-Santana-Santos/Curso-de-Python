# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).



contador = 0
soma = 0
numero = 0

while numero != 999:
    numero = int(input("Digite um número (tecle 999 para sair): "))
    if numero != 999:
        contador += 1
        soma += numero

print("Você digitou {} números. O Resultado total é de {}".format(contador, soma))

