#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print(" Invertido: \033[0:35m {} \033[0m  | \033[0:35m {} \033[0m é um palindromo.".format(inverso, frase))
else:
    print("\033[0:31m {} \033[0m Não é um palindromo.".format(frase))