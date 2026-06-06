#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao:  "))
decimo = termo1 + (10 - 1) * razao

for c in range(termo1, decimo + razao, razao):
    print(c,end=" ")
print("Acabou!")
