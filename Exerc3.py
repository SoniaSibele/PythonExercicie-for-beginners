#Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os 
#valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: 
#equilátero, isósceles ou escaleno.
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
    
# Testar se é triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
elif (a == b) and (a == c) :
        print('Equilatero-três lados iguais')
elif (a==b) or (a==c) or (b==c):
        print('Isósceles-dois lados iguais')
else:
        print('Escaleno-três lados diferentes')

