# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import time, math

t_start = time.time()

def is_pythagorean(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def is_sum(a, b, c, x):
    if a + b + c == x:
        return True
    else:
        return False

num = 1000


for i in range(1, num):
    for j in range(2, num - i):
        k = math.sqrt(i*i + j*j)
        if i + j + k > num:
            break
        #print('\33[32m', "a=", i, " b=", j, " c=", int(k), '\33[0m', sep="")
        if is_pythagorean(i, j, int(k)) and is_sum(i, j, int(k), num):
            print()
            print('\33[32m', i * j * k, '\33[0m', sep="")
            print('\33[32m', "a=", i, " b=", j, " c=", int(k), '\33[0m', sep="")
            print('\33[91;1m', "runtime = ", str(time.time() - t_start)[0:6], "s", '\33[0m', sep="")
            exit()