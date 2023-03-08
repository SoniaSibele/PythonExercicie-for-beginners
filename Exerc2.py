#Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 
#2- Segunda, etc.). Se digitado outro valor deve aparecer uma menagem de erro.
dia_semana = int(input('Digite um número de (1 a 7): '))

if dia_semana == 1:
    print('Segunda-Feira')

elif dia_semana == 2:
    print('Terça -Feira')

elif dia_semana == 3:
    print('Quarta-Feira')

elif dia_semana == 4:
    print('Quinta-Feira')

elif dia_semana == 5:
    print('Sexta-Feira')

elif dia_semana == 6:
    print('Sabado')

elif dia_semana == 7:
    print('Domingo')

else:
    print('Dia não encontrado.')
