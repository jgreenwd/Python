##Exercise 3.3. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
  return '{:>70}'.format(s)

##Exercise 3.4.
#2 Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.

def do_twice(f,val):
  f(val)
  f(val)

#3 Write a more general version of print_spam, called print_twice, that takes a string as a parameter and prints it twice.

def print_twice(s):
  print(s)
  print(s)

#4 Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.

do_twice(print_twice,'spam')

#5 Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

def do_four(f,val):
  do_twice(f,val)
  do_twice(f,val)

