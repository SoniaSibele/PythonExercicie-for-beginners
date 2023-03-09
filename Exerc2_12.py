# Escreva um programa que lê uma string e determina se a mesma é um palíndromo.
def is_palindrome(string):
 
  string = string.replace(" ", "").lower()
  reversed_string = string[::-1]

  return string == reversed_string

# test the function
print(is_palindrome("mama"))  # True
print(is_palindrome("hello"))  # False
