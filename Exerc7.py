#Uma fruteira está vendendo frutas com a seguinte tabela de preços....

morangos = int(input("Digite a quantidade de morangos [kg]: "))
macas = int(input("Digite a quantidade de maças [kg]: "))
preco_morango1 = morangos * 250
preco_morango2 = morangos * 220

preco_maca1 = macas * 180
preco_maca2 = macas * 150
print("Quantidade de maçãs: ", macas, "\nQuantidade de morangos: ", morangos)
if morangos < 5:
    preco_morango = preco_morango1
    print("Preço dos moragos: ", preco_morango)
else:
    preco_morango = preco_morango2
    print("Preço dos moragos: ", preco_morango2)

if macas < 5:
    preco_maca = preco_maca1
    print("Preço das maçãs: ", preco_maca)
else:
    preco_maca = preco_maca2
    print("Preço das maçãs: ", preco_maca2)

preco_total = preco_maca + preco_morango
if preco_total > 2500 or (macas + morangos) > 8:
    print("Preço total: ", (preco_total - (preco_total * 0.1)))
else:
    print("Preço total: ", preco_total)
