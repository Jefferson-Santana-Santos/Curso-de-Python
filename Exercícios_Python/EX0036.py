# Escreva um programa  para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar  o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos deseja pagar: "))

# cálculo da prestação mensal
prestacao_mensal = valor_casa / (anos * 12)

# limite de 30% do salário
limite = salario * 30 / 100

print(f"Valor da prestação mensal: R$ {prestacao_mensal:.2f}")
print(f"Limite permitido: R$ {limite:.2f}")

if prestacao_mensal <= limite:
    print(" Empréstimo aprovado!")
else:
    print(" Empréstimo negado. A prestação excede 30% do salário.")
