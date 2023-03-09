#desenvolver um programa que leia as um 
#conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperatura 
#informadas, bem como a média das temperaturas. A
temp = [-10, -8, 0, 1, 2, 5, -2, -4]
mínima = temp[0]  # temp  minima primeiro elemento da lista 
máxima = temp[0]
soma = 0
for i in temp:
    if i < mínima:
        mínima = i
    if i > máxima:
        máxima = i
    soma = soma + i
print(f"Temperatura máxima: {máxima} °C")
print(f"Temperatura mínima: {mínima} °C")
print(f"Temperatura média: {soma / len(temp)} °C")
