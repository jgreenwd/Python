# Reinforcement
# R-1.1
def is_multiple(n, m):
    return n % m == 0


# R-1.2
def is_even(k):
    digit = str(k)[-1]

    return digit in ['0','2','4','6','8']


# R-1.3
def minmax(data):
    import math
    lo = math.inf
    hi = -math.inf
    for val in data:
        if val > hi:
            hi = val
        if val < lo:
            lo = val

    return (lo, hi)


# R-1.4
def sum_of_squares(n):
    sum = 0
    n -= 1
    while n > 0:
        sum += n**2
        n -= 1

    return sum


# R-1.5
def sum_of_squares2(n):
    return sum([x**2 for x in range(0, n)])


# R-1.6
def sum_of_squares_for_odds(n):
    sum = 0
    n = n-1 if n % 2 == 0 else n-2
    while n > 0:
        sum += n**2
        n -= 2

    return sum


# R-1.7
def sum_of_squares_for_odds2(n):
    return sum([x**2 for x in range(0, n) if x % 2 == 1])


# R-1.8
# given len(s) == n
# s[k]      -n <= k < 0
# s[j]      len(s)-1 >= j > 0


# R-1.9
# assuming the values in question are inclusive: 51, 61, 71, & 81


# R-1.10
# assuming the values are inclusive: range(8, -10, -2)


# R-1.11
# [2**x for x in range(9)]


# R-1.12
def my_rand_range(arr):
    from random import randrange

    return arr[randrange(len(arr))]

print(my_rand_range([1,2,3]))
