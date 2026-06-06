#crie um programa que pergunta a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
#para viagens de até 200 km.  E R$ 0,45 para viagens mais longes.

distancia = float(input("Digite a distância da sua viagem (km): "))

if distancia <= 200:
    resultado = distancia * 0.50   # até 200 km
else:
    resultado = distancia * 0.45   # acima de 200 km

print("A distância da sua viagem é {} Km. O custo da passagem é R$ {:.2f}".format(distancia, resultado))
