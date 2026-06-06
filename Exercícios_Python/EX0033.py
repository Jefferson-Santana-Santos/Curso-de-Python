
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Descobre o maior e o menor usando funções prontas
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print("Os números digitados foram: {}, {}, {}.".format(n1, n2, n3))
print("O maior número é: {}".format(maior))
print("O menor número é: {}".format(menor))
