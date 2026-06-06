#65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


continuar = "S"
contador = 0
soma = 0
maior = 0
menor = 0

while continuar in "S":
    numero = int(input("Digite um número: "))
    contador += 1
    soma = soma + numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input(" Deseja continuar? [S/N] ")).upper().strip()[0]

media = soma / contador
print("O Maior número digitado foi {} e o Menor é {}.".format(maior, menor))
print (" Você digitou {} números. A média dos valores é {:.2f}.".format(contador,media))

