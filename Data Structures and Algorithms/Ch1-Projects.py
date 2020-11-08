# Projects

# P-1.29
def p1_29():
    from itertools import permutations as perm
    test_string = ['c','a','t','d','o','g']

    print('All permuations of the letters in "catdog": \n')

    for x in perm(test_string, 6):
        print(x)


# P-1.30
def p1_30():
    import string

    while n := input('Enter a number greater than 2: \n>'):
        for ch in n:
            if ch not in string.digits:
                print(f'Invalid input: {ch}')
        n = int(n)
        if n < 2:
            print(0)
            break
        break

    i = 0

    while 2**i < n:
        i += 1

    print(f'Result: {i if n == 2**i else i-1}')


# P-1.31
def p1_31(cost, paid):
    change = paid - cost

    currency = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.5, 0.01]

    result = dict()

    for val in currency:
        if change >= val:
            result["$" + str(val)] = change // val
            change -= result["$" + str(val)] * val

    return result


# P-1.32
def p1_32():
    from string import digits

    operations = '+-*/'
    terms = []

    while(n:= input('>')):
        if n not in digits + operations:
            print(f'Invalid entry: {n}')
        else:
            terms.append(n if n in operations else int(n))
            if len(terms) == 3:
                if terms[1] == '+':
                    terms[0] = terms[0] + terms[2]
                elif terms[1] == '-':
                    terms[0] = terms[0] - terms[2]
                elif terms[1] == '*':
                    terms[0] = terms[0] * terms[2]
                elif terms[1] == '/':
                    terms[0] = terms[0] / terms[2]
                terms = terms[:1]
                print(f'>{terms[0]}')


# P-1.34
def p1_34():
    from random import randint
    from string import ascii_lowercase
    output = 'I will never spam my friends again.'

    counter = 0
    for i in range(100):
        x = randint(i, 1000)
        if x < 200 and counter < 8:
            tmp = output
            idx = randint(0, len(output)-2)
            letter = randint(0, len(ascii_lowercase)-1)
            tmp = tmp[:idx-1] + ascii_lowercase[letter] + tmp[idx:]
            counter += 1
            print(f'{i+1:3} {tmp}')
        else:
            print(f'{i+1:3} {output}')


# P-1.35
def p1_35():
    from random import randint
    from numpy import unique

    for n in range(5,101,5):
        # n choose 2
        comparisons = n * (n-1) / 2

        # assign n- random days in the year as birthdays
        bdays = [randint(0, 366) for x in range(n)]

        # if duplicates exist
        if len(unique(bdays)) < len(bdays):
            print(f'{n:3} - \tcomparisons: {int(comparisons):4}\tprobability: {comparisons / 366:1.3f}')
