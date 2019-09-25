## Exercise 9.7 Given a list of words, write a program to find any words with 3 or more sets of consecutive pairs of letters: "mmeeii"
## Big-O of 2n vs. book solution Big-O of n.

def consecutive_double_letters(word):
  start_indexes_of_doubles = []

  for index, letter in enumerate(word):
    if index < len(word) - 1 and letter == word[index + 1]:
      start_indexes_of_doubles.append(index)

  consecutives = 1
  counter = 1
  while counter < len(start_indexes_of_doubles):
    if start_indexes_of_doubles[counter - 1] + 2 == start_indexes_of_doubles[counter]:
      consecutives += 1
    counter += 1

  return consecutives

words = open("words.txt")

if words.readable:
  for word in words:
    count = consecutive_double_letters(word)
    if count > 2:
      print(word,)

words.close

## Exercise 9.8 Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements:
##      1. the last 4 digits of n are palindromic
##      2. the last 5 digits of n+1 are palindromic
##      3. the middle 4 digits of n+2 are palindromic
##      4. all 6 digits of n+3 are palindromic
