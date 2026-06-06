#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salários superiores a R$ 1.250.00, calcule um aumento de 10%
#para salários inferiores ou iguais, o aumento é de 15%

#Versão que permite o usuário digitar qual a porcentagem ele quer

from colorama import Fore,Style
salario = float(input("Digite seu salário : "))
porcentagem = float(input("Digite a porcentagem do aumento: "))
calculo = salario + (salario * porcentagem / 100)

print("O aumento foi de " +
      Fore.GREEN + "{:.1f}".format(porcentagem) + Style.RESET_ALL +
      " %. Seu novo salário é de R$ {:.2f}".format(calculo))