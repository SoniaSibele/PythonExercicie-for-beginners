#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério
# baseado no salário atual
salario = float(input("Digite o seu salário: "))

if (salario <=  18.000):
        percentual = 20
elif (salario <=  27.000):
        percentual = 15
elif (salario <=  45.000):
        percentual = 10
else:
        percentual = 5

print('Salario original: ', salario,'$')
print('Percentagem aplicada: ',percentual,'%')

percentual = percentual/100
aumento = percentual * salario
novo_salario = salario + aumento
    
print('Valor de Aumento: ',aumento, '$')
print('Salario após o aumento: ', novo_salario, '$')