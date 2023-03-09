#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo utilizador
print("Cálculo do fatorial de um número")
n = int(input("Digite um número inteiro não-negativo: "))
def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1) 
result = fatorial(n)
print(result)

