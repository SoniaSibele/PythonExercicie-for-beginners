#Crime...
pontos = 0 #contador de repostas positivas

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?',
             'Mora perto da vítima?', 'Devia para a vítima?',
             'Já trabalhou com a vítima?']
for pergunta in perguntas:

   print(pergunta)
   resposta = input('Responda sim ou não:  ').lower( ).replace( 'ã' , 'a' ) #Pedeir reposta; evitar letras maiúsculas ou ã.

   if resposta == 'sim':

       pontos = pontos +1 
if pontos < 2:
    print("Esta pessoa é inocente")
if pontos == 2:
    print("Esta pessoa é suspeita")
elif pontos < 5:
    print("Esta pessoa é cúmplice")
else:
    print("Esta pessoa é assassino")
       