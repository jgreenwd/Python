## Exercise 8.10 Write a one-line version of is_palindrome from Exercise 6.6 using string slice [::-1]

def is_palindrome(args):
  return args == args[::-1]
  
## Exercise 8.12 Write a function called rotate_word that takes a string and an integer as parameters, and that returns a new string that contains the letters from the original string “rotated” by the given amount.

def rotate_word(s, i):
  output = []
  for letter in s:
    val = ord(letter) + i
    if (letter.islower() and val > ord('z')) or (letter.isupper() and val > ord('Z')):
      val -= 26
    elif (letter.islower() and val < ord('a')) or (letter.isupper() and val < ord('A')):
      val += 26
    output.append(val)

  for index, number in enumerate(output):
    output[index] = chr(number)

  return ''.join(output)
  
