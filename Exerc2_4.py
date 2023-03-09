#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 
#1 a 10. O utilizador deve informar de qual numero ele deseja ver a tabuada
numero = int(input("Digite um numero de 1 a 10: "))
for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")

