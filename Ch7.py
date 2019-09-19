##Exercise 7.2. Encapsulate this loop in a function called square_root that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.

def square_root(a):
  x = a/2
  while True:
    y = (x + a/x) / 2
    if abs(y-x) < 0.000001:
      return x
    x = y
    
##Exercise 7.3. To test the square root algorithm in this chapter, you could compare it with math.sqrt. Write a function named test_square_root that prints a table

def test_square_root(limit):
  a = 1.0
  while a < limit:
    b = square_root(a)
    c = math.sqrt(a)
    d = abs(b-c)
    print(a,'{:15.10f}'.format(b),'{:15.10f}'.format(c),'{:15.12f}'.format(d))
    a += 1
    
##Exercise 7.4 Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result. It should continue until the user enters 'done', and then return the value of the last expression it evaluated.

def eval_loop():
  response = input('Enter an expression to evaluate: ')
  while response != 'done':
    print(eval(response))
    response = input('Enter an expression to evaluate: ')
  return response

##Exercise 7.5 Write a function called estimate_pi that uses this formula to compute and return an estimate of π. It should use a while loop to compute terms of the summation until the last term is smaller than 1e-15 (which is Python notation for 10−15).

def estimate_pi():
  constant = (2 * math.sqrt(2)) / 9801
  total = 0
  k = 0

  while True:
    numerator = math.factorial(4*k) * (1103 + 26390 * k)
    denominator = (math.factorial(k)**4) * 396**(4*k)
    term = constant * (numerator / denominator)
    total += term
    if abs(term) < 1e-15: break
    k += 1

  return 1 / total
