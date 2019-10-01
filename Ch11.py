## Exercise 11.9 Use a dictionary to write a faster, simpler version of has_duplicates from Exercise 10.8

def has_duplicates(l):
  return len(set(l)) < len(l)
  
## Exercise 11.10 Write a program that reads a wordlist and finds all the rotate pairs.

