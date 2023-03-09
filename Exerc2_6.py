#Fibonacci
#A sequência inicia com 0 e 1, e os números seguintes serão a soma dos dois números anterior.
#anterior = 0
#proximo = 0
n = int(input("Introduz o valor de n: "))
def fibo(n):
    if n==1:
      return 0
    
    elif n==2:
      return 1
    else:
      return fibo(n-1) + fibo(n-2)   

resultado = fibo(n)
print(resultado )


