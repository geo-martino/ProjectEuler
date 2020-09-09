# What is the value of the first triangle number to have over five hundred divisors?

from time import time
from functools import reduce

t_start = time()

def triangle(n):
    tri = 0
    for i in range(n+1):
        tri += i
    return tri

"""
def factors(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
    for i in range(len(factors) - 1, -1, -1):
        factors.append(n // factors[i])
    return factors
"""

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

i = 1
sum = 0
while i:
    if len(factors(triangle(i))) < 500:
        i +=1
    else:
        print('\33[32m', '1st Triangle no. with > 500 factors = {} ({}th)'.format(triangle(i), i), '\33[0m', sep="")
        print('\33[91;1m', "runtime = ", str(time() - t_start)[0:7], "s", '\33[0m', sep="")
        break


