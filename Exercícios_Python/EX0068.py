#68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
v=0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador  {computador}. Total de {total}", end= " ")
    print(" Deu PAR" if total %2 == 0 else "Deu ÍMPAR")
    if tipo == "P":
        if jogador % 2 == 0:
            print("Você VENCEU !!")
            v += 1
        else:
            print("Você PERDEU !!")
            break

    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU !!")
        else:
            print("Voce PERDEU !!")

    print("Vamos jogar novamente...")
print("GAME OVER! Você venceu {} vezes".format(v))
