## Exercise 10.6 Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.

def is_sorted(l):
  index = 0
  while index < len(l) - 1:
    if l[index] > l[index + 1]:
      return False
    index += 1
  return True
  
## Exercise 10.7 Write a function called is_anagram that takes two strings and returns True if they are anagrams.
  
def is_anagram(s1, s2):
  return sorted(s1.replace(' ','')) == sorted(s2.replace(' ',''))

## Exercise 10.8 1. Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

def has_duplicates(l):
  for item in l:
    if l.count(item) > 1:
      return True
  return False

## Exercise 10.9 Write a function called remove_duplicates that takes a list and returns a new list with only the unique elements from the original.

def remove_duplicates1(l):
  l = sorted(l)

  index = len(l) - 1
  while index > 0:
    if l[index] == l[index -1]:
      l.pop(index)
    index -= 1

  return l

def remove_duplicates2(l):
  return list(set(l))
  
## Exercise 10.10 Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x].
  
def load_words1():
  fin = open("words.txt")
  words = []
  if fin.readable:
    for word in fin:
      words.append(word)
  fin.close
  print(len(words))

def load_words2():
  fin = open("words.txt")
  words = []
  if fin.readable:
    for word in fin:
      words += [word]
    fin.close
    print(len(words))

# In this case, the run times are virtually identical. If load_words2() used "words = words + [word]", the run time would be significantly increased

## Exercise 10.11 Write a function called bisect that takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or None if it’s not.

# recursive implementation of binary sort doesn't work in this instance because of the need to pass a sub-list, which results in different indexes for the list values

def bisect(l,val):
  upper_bound = len(l) - 1
  lower_bound = 0

  index = int((upper_bound - lower_bound) / 2)
  while True:
    print(lower_bound, index, upper_bound)
    if val == l[index]:                                           #if value is found at index
      return index
    elif upper_bound == index == lower_bound or upper_bound < 0:  #if value not found
      return -1
    elif val < l[index]:                                          #if value in lower half, lower the ceiling
      upper_bound = index - 1
      index = int((upper_bound - lower_bound) / 2) + lower_bound
    elif val > l[index]:                                          #if value in upper half, raise the floor
      lower_bound = index + 1
      index = int((upper_bound - lower_bound) / 2) + lower_bound

# solution using bisect module

def bisect(sequence, args):
  from bisect import bisect_left
  index = bisect_left(sequence, args)
  
  if sequence[index] == args:
    return index
  return -1

## Exercise 10.12 Write a program that finds all the reverse pairs in the word list.

def reverse_exists(l,s):
  return s[::-1] in l

fin = open("words.txt")
words = []
reverse_list = []
for item in fin:
  word = item.strip()
  if reverse_exists(words, word):
      reverse_list.append(word)
  words.append(word)

fin.close

## Exercise 10.13
# 1. Write a program that finds all pairs of words that interlock.

def interlock_size_valid(s1,s2):
  if len(s1) >= len(s2):
    return True
  return False

def interlock(s1,s2):
  if interlock_size_valid(s1,s2):
    counter = 0
    new_word = str()
    while counter < len(s1):
      new_word += s1[counter]
      if counter < len(s2):
        new_word += s2[counter]
      counter += 1
    return new_word
