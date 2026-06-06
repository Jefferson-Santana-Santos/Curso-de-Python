# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.


numero = int(input("Digite o  número "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5
print(" O dobro  de {} é  {}  o triplo de {} é  {}  e sua raiz quadrada é  {:.2f}  " .format(numero,dobro, numero,triplo, raiz))
