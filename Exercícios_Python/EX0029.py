#crie um programa que se ultrapassar 80 km, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limtie.


n1 = float(input(" Digite a velocidade do veículo! \n "))
m = float(7.00)
if n1 > 80:
    excesso = n1 - 80
    valor_multa = excesso * m
    print("Você foi multado!")
    print("Sua multa é de: R${:.2f} !".format(valor_multa))

else:
    print("Você não foi multado!")

