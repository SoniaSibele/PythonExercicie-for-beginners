#s= str(input("Digite uma palavra: "))
#def isPalindrome(s):
    #return s == s[::-1]
  
#ans = isPalindrome(s)
  
#if ans:
    #print("Yes")
#else:
    #print("No")

def is_palindrome(string):
  # remove any spaces and make all characters lowercase
  string = string.replace(" ", "").lower()

  # reverse the string
  reversed_string = string[::-1]

  # check if the string is equal to its reverse
  return string == reversed_string

# test the function
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
