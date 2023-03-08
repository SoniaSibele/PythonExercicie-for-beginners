#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao utilizador o valor 
#a ser levantado e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis são de 200, 500, 1.000, 2.000, 5.000 escudos. O valor mínimo é de 200 escudos e o 
#máximo de 20.000 escudos. O programa não deve se preocupar com a quantidade de notas 
#existentes na máquina. 

print("Valor mínimo a ser levantado: 200$.")
print("Valor máximo a ser levantado: 20.000$.")
saque = int(input("Valor do a ser levantado: ")) 

while(saque<200) or (saque>20000):
    print("Valor fora dos intervalos.")
    saque = int(input("Digite novamente: "))

if(saque>=200) and (saque<=20000):
    
    cinco_mil = int(saque / 5000)
    saque = saque - (cinco_mil*5000)

    dois_mil = int(saque/2000)
    saque = saque - (dois_mil*2000)

    mil = int(saque/1000)
    saque = saque - (mil*1000)

    quinhentos = int(saque/500)
    saque = saque - (quinhentos*5)

    duzentos = int(saque/500)
    saque = saque - (duzentos*200)

    print('Notas de 5000,00 = ',cinco_mil)
    print('Notas de 2000 = ',dois_mil)
    print('Notas de 1000 = ',mil)
    print('Notas de 500 = ',quinhentos)
    print('Notas de 200 = ',duzentos)
