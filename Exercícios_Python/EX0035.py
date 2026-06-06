#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

r1 = float(input("Insira um valor: "))
r2 = float(input("Insira um valor: "))
r3 = float(input("Insira um valor: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Pode formar um triângulo!")

else:
    print("Não pode formar um triângulo!")