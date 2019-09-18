##Exercise 5.3
#1. Write a function named check_fermat that takes four parameters - a,b,c, and n - and that checks that Fermat's theorem holds. If n is greater than 2 and it turns out to be true that a^n + b^n == c^n the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”

def check_fermat(a,b,c,n):
  if n > 2:
    if a**n + b**n == c**n:
      print('Holy smokes, Fermat was wrong!')
    else:
      print("No, that doesn't work.")
      
#2. Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.

def gather_input():
  a = int(input('Enter number for (a): '))
  b = int(input('Enter number for (b): '))
  c = int(input('Enter number for (c): '))
  n = int(input('Enter number for (n): '))
  check_fermat(a,b,c,n)
  
##Exercise 5.4
#1. Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks with the given lengths.

def is_triangle(a,b,c):
  nums = [a,b,c]
  nums.sort()
  if nums[0] + nums[1] < nums[2]:
    print('No')
  else:
    print('Yes')
    
#2. Write a function that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to check whether sticks with the given lengths can form a triangle.

def gather_input():
  a = int(input('Enter length for side a: '))
  b = int(input('Enter length for side b: '))
  c = int(input('Enter length for side c: '))
  is_triangle(a,b,c)
