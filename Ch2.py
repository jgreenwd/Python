#NOTE: I am using Python 3, so integer division produces floats

##Exercise 2.2. Assume that we execute the following assignment statements:
width = 17
height = 12.0
delimiter = '.'
#For each of the following expressions, write the value of the expression and the type (of the value of the expression).
#1. width/2             #value == 8.5     #type == float
#2. width/2.0           #value == 8.5     #type == float
#3. height/3            #value == 4.0     #type == float
#4. 1 + 2 * 5           #value == 11      #type == int
#5. delimiter * 5       #value = '.....'  #type == str

##Exercise 2.3. Practice using the Python interpreter as a calculator:
#1. The volume of a sphere with radius r is (4/3)πr^3. What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!

import math
print((4/3) * math.pi * 5**3)

#2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

number_ordered = 60
book_cost = 24.95 * 0.6 * number_ordered
shipping = 3 + (number_ordered - 1) * 0.75
print(book_cost + shipping)

#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

hours = 6
minutes = 52
seconds = 0

time1 = '8:15'
time2 = '7:12'
time3 = '7:12'
time4 = '7:12'
time5 = '8:15'

def add_time(time):
  colon = time.find(':')
  secs = int(time[colon+1:])
  mins = int(time[:colon])
  global seconds
  seconds += secs
  global minutes
  minutes += mins
  update_time()

def update_time():
  global seconds
  global minutes
  global hours
  if seconds > 59:
    minutes += int(seconds / 60)
    seconds %= 60

  if minutes > 59:
    hours += int(minutes / 60)
    minutes %= 60

  if hours > 12:
    hours %= 12

add_time(time1)
add_time(time2)
add_time(time3)
add_time(time4)
add_time(time5)

time_output = str(hours) + ':' + '{:02}'.format(minutes) + ':' + '{:02}'.format(seconds)

print(time_output)
