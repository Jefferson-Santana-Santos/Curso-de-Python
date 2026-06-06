# Escreva um programa que leia um valor em metros e o exiba convertido a milìmetros

metros = float(input("Digite o  número em metros "))
centimetro = metros * 100
milimetro = metros * 1000

print(" O valor {:.2f} em metros corresponde à {:.2f} em centímetros e {:.2f} em milímetros." .format(metros,centimetro, milimetro))
