""" Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""



opcao = False
while not opcao:

    opcao = int(input("{:=^40}".format("==== MENU ====") + """
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa 
    Digite uma opção:  """ ))
    print("{:=^40}".format("========"))
    if opcao not in range (1,6):
        print("Digite uma opção válida! ")
        opcao = False

    match opcao:
        case 1:
            soma_op1 = int(input("Digite o primeiro valor: "))
            soma_op2 = int(input("Digite o segundo valor: "))
            resultado = soma_op1 + soma_op2
            print("O Resultado é {}".format(resultado))
            saida = str(input("Deseja realizar outra operação S/N?: ")).strip().upper()
            if saida == "S":
                opcao = False
            else:
                opcao = True
                print("Obrigado por utilizar o programa!")

        case 2:
            multiplicar_op1 = int(input("Digite o primeiro valor: "))
            multiplicar_op2 = int(input("Digite o segundo valor: "))
            resultado = multiplicar_op1 * multiplicar_op2
            print("O Resultado é {}".format(resultado))
            saida = str(input("Deseja realizar outra operação S/N?: ")).strip().upper()
            if saida == "S":
                opcao = False
            else:
                opcao = True
                print("Obrigado por utilizar o programa!")

        case 3:
            maior_op1 = int(input("Digite o primeiro valor: "))
            maior_op2 = int(input("Digite o segundo valor: "))
            resultado = max(maior_op1,maior_op2)
            print("O Maior número é {}".format(resultado))
            saida = str(input("Deseja realizar outra operação S/N?: ")).strip().upper()
            if saida == "S":
                opcao = False
            else:
                opcao = True
                print("Obrigado por utilizar o programa!")

        case 4:
            # Redefinir os números e já permitir nova operação
            novos_numeros1 = int(input("Digite o novo primeiro valor: "))
            novos_numeros2 = int(input("Digite o novo segundo valor: "))
            print("Novos números definidos: {} e {} ".format(novos_numeros1, novos_numeros2))


            sub_opcao = (int(input("""
            O que deseja fazer com os novos números?
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            Digite uma opção: """)))

            if sub_opcao == 1:
                print("Resultado da soma:", novos_numeros1 + novos_numeros2)
            elif sub_opcao == 2:
                print("Resultado da multiplicação:", novos_numeros1 * novos_numeros2)
            elif sub_opcao == 3:
                print("Maior número:", max(novos_numeros1, novos_numeros2))

            saida = str(input("Deseja realizar outra operação S/N?: ")).strip().upper()
            if saida == "S":
                opcao = False
            else:
                opcao = True
                print("Obrigado por utilizar o programa!")

        case 5:
            print("Obrigado por utilizar o programa!")












