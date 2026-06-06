#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.


# Programa que mostra termos de uma PA e permite continuar

termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

contador = 1
termo = termo1
total = 0
mais = 10  # começa mostrando 10 termos

while mais != 0:
    total += mais
    while contador <= total:
        print("{}".format(termo), end=" ")
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? (Digite 0 para encerrar): "))

print("Progressão finalizada com {} termos mostrados.".format(total))
