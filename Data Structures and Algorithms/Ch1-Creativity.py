# Creativity

# C-1.13
# def reverse(list):
    # tmp = copy of list
    # i = 0
    # while i < midway point of tmp:
        # tmp[i], tmp[-1 - i] = tmp[-1 -i], tmp[i]
        # i += 1
    # return tmp

# Python implementation is probably something more like:
# def reverse(arr):
    # return arr[::-1]


# C-1.14
def find_odd_pair(arr):
    for x in arr:
        for y in arr:
            if x != y:
                if (x * y) % 2 == 1:
                    return x, y


# C-1.15
def unique(arr):
    for x in range(0, len(arr)):
        for y in range(x+1, len(arr)):
            if arr[x] == arr[y]:
                return False

    return True


# C-1.16
# The implementation of scale passes a reference to a list as a parameter, not an alias.


# C-1.17
# If we define "properly" to mean that the elements of the list are scaled, then no. It does not. After execution, the changes move out of scope.
# However, if we define properly as not having any side-effects, then yes. It does.


# C-1.18
val = 0
result = []
for x in [x*2 for x in range(10)]:
    val += x
    result.append(val)

# C-1.19
# import string
# print([x for x in string.ascii_lowercase])

# C-1.20
def my_shuffle(arr):
    from random import randint
    local_arr = arr.copy()

    for idx in range(len(local_arr)):
        a = randint(0, len(local_arr)-1)
        local_arr[idx], local_arr[a] = local_arr[a], local_arr[idx]

    return local_arr

# C-1.21
# user_in = []

# try:
    # while (s := input('>')):
        # user_in.append(s)
# except EOFError:
    # print('\n')
    # for x in user_in[::-1]:
        # print(x)


# C-1.22
def dot_product(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    
    return result


# C-1.23
try:
    l = [1,2,3]
    l[3] = 4
except IndexError:
    print("Don't try buffer overflow attacks in Python!")


# C-1.24
def vowel_count(s):
    num = 0
    for x in s:
        if x in ['a','e', 'i', 'o', 'u']:
            num += 1
    
    return num


# C-1.25
def punctuation_stripper(s):
    from string import punctuation as punc
    return ''.join(list(filter(lambda x: x not in punc, s)))


# C-1.26
# try:
    # user_in = []
    # while (len(user_in) <= 2):
        # user_in.append(int(input('>')))
    # print(f'{user_in[0]} + {user_in[1]} = {user_in[2]} is {user_in[0] + user_in[1] == user_in[2]}')
    # print(f'{user_in[0]} - {user_in[1]} = {user_in[2]} is {user_in[0] - user_in[1] == user_in[2]}')
    # print(f'{user_in[0]} * {user_in[1]} = {user_in[2]} is {user_in[0] * user_in[1] == user_in[2]}')
    # print(f'{user_in[0]} / {user_in[1]} = {user_in[2]} is {user_in[0] / user_in[1] == user_in[2]}')
# except ValueError:
    # print('Only integers allowed.')


# C-1.27
def factors(n):
    k = 1
    while k <= n:
        if n % k == 0:
            yield k
        k += 1
    if k * k == n:
        yield k


# C-1.28
def norm(v, p=None):
    from math import sqrt
    if p == None:
        p = 2
    return (sum([x**p for x in v]))**(1/p)
