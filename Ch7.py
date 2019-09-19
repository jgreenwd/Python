##Exercise 7.2. Encapsulate this loop in a function called square_root that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.

def square_root(a):
  x = a/2
  while True:
    y = (x + a/x) / 2
    if abs(y-x) < 0.000001:
      return x
    x = y
    
##Exercise 7.3. To test the square root algorithm in this chapter, you could compare it with math.sqrt. Write a function named test_square_root that prints a table
