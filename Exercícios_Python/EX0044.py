#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:


# 1 - à vista dinheiro/cheque: 10% de desconto
# 2 -  à vista no cartão: 5% de desconto
# 3 - em até 2x no cartão: preço formal
# 4 - 3x ou mais no cartão: 20% de juros




print("{:=^40}".format("LOJAS SANTANA"))
nome_produto = str(input("Digite o nome do produto: ")).upper()
valor_produto = float(input("Digite o valor do produto R$: "))
vezes_parcela = int(input("Digite a quantidade de parcelas: "))


print("-=-="*20)
print("{:^40}".format("LOJAS SANTANA"))
opcao = int(input(""" Escolha a opção
 [0] Sair   
 [1] À vista dinheiro/cheque: 10% de desconto 
 [2] À vista no cartão: 5% de desconto
 [3] Em até 2x no cartão
 [4] 3x ou mais no cartão: 
  Digite uma opção:   """))
print("-=-="*20)


desconto_dinheiro_10 = valor_produto - (valor_produto * 10 / 100)
desconto_cartao_5 = valor_produto - (valor_produto * 5 / 100)
juros_cartao_20 = valor_produto + (valor_produto * 20 / 100)
valor_parcela = valor_produto / vezes_parcela


if opcao == 1:
    print("Produto: {} | Valor S/desconto: R$ {:.2f} | Valor da parcela {:.2f} | Valor final com desconto 10%: R$ \033[0:32:40m {:.2f} \033[0m ".format(nome_produto, valor_produto,valor_parcela,desconto_dinheiro_10 ))

elif opcao == 2:
    print("Produto: {} | Valor s/desconto: R$ {:.2f} | Valor final com desconto 5%: R$ \033[0:32:40m {:.2f} \033[0m ".format(nome_produto, valor_produto,desconto_cartao_5))

elif opcao == 3:
    print("Produto: {} | Valor s/desconto: R$ {:.2f} | Valor da parcela R$ {:.2f} | Valor final com desconto: R$ \033[0:36:40m {:.2f} \033[0m ".format(nome_produto, valor_produto,valor_parcela,valor_produto))

elif opcao == 4:
    print("Produto: {}  | Valor s/desconto: R$ {:.2f} | Valor da parcela R$ {:.2f} | Valor final juros + 20%: R$ \033[0:31:40m {:.2f} \033[0m ".format(nome_produto, valor_produto, valor_parcela, juros_cartao_20))

elif opcao == 0:
    print("Obrigado por utilizar nossos serviços !")

else:
    print("\033[0:31:40mOpção inválida\033[0m !")






