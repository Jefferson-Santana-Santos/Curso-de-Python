#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salários superiores a R$ 1.250.00, calcule um aumento de 10%
#para salários inferiores ou iguais, o aumento é de 15%


salario = float(input("Digite seu salário : "))
if salario > 1250:
    salario = salario * 1.10
    print("O aumento é de 10%. Seu salário atualizado é de R$ {:.2f}  ".format(salario))

else:
    salario = salario * 1.15
    print("O aumento é de 15%. Seu salário atualizado é de R$ {:.2f} ".format(salario))