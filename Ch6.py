##Exercise 6.1. Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.

def compare(x,y=0):
  if x != y:
    if x > y:
      return 1
    else:
      return -1
  else:
    return 0
      
##Exercise 6.2. Use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go.

def hypotenuse(s1, s2):
  import math
  return math.sqrt(s1**2 + s2**2)

##Exercise 6.3. Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.
  
def is_between(x,y,z):
    return x <= y <= z
  
##Exercise 6.5
# Write a function named ack that evaluates Ackermann’s function. Use your function to evaluate ack(3, 4), which should be 125. 

def ack(m,n):
  if m == 0:
    return n + 1
  elif m > 0 and n == 0:
    return ack(m-1, 1)
  elif m > 0 and n > 0:
    return ack(m-1, ack(m, n-1))
    
## Exercise 6.6
#2. Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. Remember that you can use the built-in function len to check the length of a string.

def is_palindrome(s):
  for index in range(int(len(s)/2)):
    if s[index] != s[len(s) - index - 1]:
      return False
  return True
  
## Exercise 6.7
# Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
  
def is_power(a, b):
  if a % b == 0:
    if a == b:
      return True
    return is_power(int(a/b), b)
  return False
  
## Exercise 6.8
# Write a function called gcd that takes parameters a and b and returns their greatest common divisor.

def gcd(a,b):
  if a % b == 0:
    return b
  else:
    return gcd(b, int(a % b))
  return 1
