#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final,de acordo com a média atingida

from colorama import Fore,Style

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("Sua média é de {} !".format(media))
if media >= 7:
    print( "Parabéns," + Fore.GREEN + " Aprovado!")
elif  media >= 5 and media <= 6.9:
    print("Você está de " + Fore.LIGHTYELLOW_EX +  "Recuperação" + Style.RESET_ALL +  " Tente novamente, não desista! ")
else:
    print("Infelizmente você foi" +  Fore.RED +  " Reprovado!")

