print("1- File Duplo\n2- Alcatra\n3- Picanha\n\n")
tipo = int(input("Digite o tipo: "))
quantidade = int(input("Digite a quantidade comprada: "))
resposta = int(input("A compra será realizada com cartao Tabajara? 1(SIM) - 2(NAO): "))

if tipo == 1:
    nome = "File Duplo"
    if quantidade < 5:
        preco = quantidade * 490
    else:
        preco = quantidade * 580
        
if tipo == 2:
    nome = "Alcatra"
    if quantidade < 5:
        preco = quantidade * 590
    else:
        preco = quantidade * 680

if tipo == 3:
    nome = "Picanha"
    if quantidade < 5:
        preco = quantidade * 690
    else:
        preco = quantidade * 780

if resposta == 1:
    r = "SIM"

    desconto = ((preco * 5) /100)
    

    total = preco - desconto
else:
    r = "NAO"
    total = preco
    

print("* Carne.......................................................... %s " %nome)
print("* Quantidade..................................................... %d KG " %quantidade)
print("* Preço......................................................... %2.f $" %preco)
print("* Cartao Tabajara................................................ %s " %r)
print("* Total do desconto............................................ %2.f $" %desconto)
print("* Total com desconto............................................ %2.f $" %total)



