#IMC

peso= float(input("Digite o peso: "))
altura= float(input("Digite a altura: "))
IMC = peso / (altura)**2
print("Seu IMC é: %.2f" % IMC)

if IMC <  18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso Normal")  
elif IMC < 30:
    print("Acima do peso")  
else:
	print("Obeso")
