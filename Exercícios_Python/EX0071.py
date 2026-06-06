# 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cedula = 50


print(f"{'=========== BANCO SANTANA ===========':^40}")

valor = int(input("Qual valor quer sacar? R$ "))
total = valor
cedula = 50
total_ced = 0
while True:
    if total >= cedula:
        total -= cedula
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"Total de {total_ced} de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_ced = 0
        if total == 0:
            break
print("="*30)
print("Volte semre ao BANCO SANTANA!")

