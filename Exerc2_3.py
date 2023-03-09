#Faça um programa que leia 5 números e informe: 
# o maior número; 
# o menor número; 
# a soma dos números; 
# a média dos números. 


numeros = []
for num in range(1, 6):
    numeros.append(int(input("Digite um numero: ")))

maiorNumero = numeros[0] #maior numero é o primeiro elemento da lista 
menorNumero = numeros[0] #menor numero é o primeiro elemento da lista 
soma = 0

cont = 0
while cont < len(numeros):# enquanto contador menor que o tamanho da lista 
    if numeros[cont] > maiorNumero:
        maiorNumero = numeros[cont]
    if numeros[cont] < menorNumero:
       menorNumero = numeros[cont]
        
    soma = soma + numeros[cont]
    cont = cont + 1
    media = soma /cont
print ("O maior número é " + str (maiorNumero))
print ("O menor número é " + str (menorNumero))
print ("A soma é " + str (soma))
print ("A média é " + str (media))
