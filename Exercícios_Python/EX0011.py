# Faça um programa que leia a largura e a altura em metros,
# calcule a sua área e a quantidade de tinta necessária
# sabendo que cada litro de tinta pinta uma área de 2 m².

largura = float(input("Digite a largura em metros: "))
altura = float(input("Digite a altura em metros: "))

area = largura * altura
tinta = area / 2  # cada litro pinta 2 m²

print("A parede tem {:.2f} m² e você precisará de {:.2f} litros de tinta.".format(area, tinta))
