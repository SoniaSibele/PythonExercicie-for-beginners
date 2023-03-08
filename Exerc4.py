#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c
import math
print('Equaçao do 2o grau da forma: ax² + bx + c')

a = float(input('Introduz o valor de a: '))
if(a==0):
        print('Não é equação do segundo grau.')
else:
        b = float(input('Introduz o valor de b: '))
        c = float(input('Introduz o valor de c: '))
        delta = b*b - (4*a*c)
        if delta <0 :
                print('Delta menor que zero. A equação não possui raízes reais')
        elif delta == 0:
                raiz = -b / (2*a)
                print('O valor de delta = 0 , A raiz é = ',raiz)
        else:
            raiz1 = (-b + math.sqrt(delta) ) / (2*a)
            raiz2 = (-b - math.sqrt(delta) ) / (2*a)
            print('Raizes da equação: ',raiz1,' e ',raiz2)
            
