#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

r1 = float(input("Insira um valor: "))
r2 = float(input("Insira um valor: "))
r3 = float(input("Insira um valor: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Pode formar um triângulo! ")
    if r1 == r2 == r3:
        print("Tipo: Triângulo EQUILÁTERO ! ")
    elif r1 != r2 != r3 != r1:
        print("Tipo: Triângulo ESCALENO !")
    else:
        print("Tipo: Triângulo ISÓSCELES !")

else:
    print("Não pode formar um triângulo ! ")