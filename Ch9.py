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

def odometer_test(num):
  return (palindromic(str(num)[-4:]) and
          palindromic(str(num+1)[-5:]) and
          palindromic(str(num+2)[1:5]) and
          palindromic(str(num+3)))

def palindromic(s):
  return s == s[::-1]

for number in range(100000,999996):
  if odometer_test(number):
    print(number)
    
## Exercise 9.9 Write a Python program to determine age differences between a parent and child which yield the most palindromic ages.

output = {}
for i in range(15,45):                #age difference, assume minimum age of pregnancy of 15 and max of 45
  for j in range(i,125):              #mother's age during palindrome test
    temp = j - i 
    if str(j).zfill(3) == str(temp)[::-1].zfill(3): #test for palindromicity
      output[j] = temp

i = {}
for key,val in output.items():
  j = key - val                       #age difference between key (mother age) & value (child age)
  if j in i.keys():                   #total number of instances where that difference occurs
    i[j] += 1
  else:
    i[j] = 1
    
print(i)
