# Find the sum of all the primes below two million.

from time import time
from numpy import sum, int64

# faster sum
def sum_primes1(n):
    sieve = [1] * n
    prime_sum = 2
    for i in range(3, n, 2):
        if sieve[i] == 1:
            prime_sum += i
            for j in range(i, n, i):
                sieve[j] = 0
    return prime_sum

n = 2000000

t_start = time()
print('\33[32m', 'Sum of all primes below {} = {}'.format(n, sum_primes1(n)), '\33[0m', sep="")
print('\33[91;1m', "runtime = ", str(time() - t_start)[0:6], "s", '\33[0m', sep="")

# sum & list of primes
def sum_primes2(n):
    sieve = [1] * n
    for i in range(2, n, 1):
        if sieve[i] == 1:
            for j in range(i*2, n, i):
                sieve[j] = 0
    primes = [0] * (sum(sieve) - 2)
    k = 0
    for j in range(2, n):
        if sieve[j] == 1:
            primes[k] = j
            k += 1
    prime_sum = sum(primes, dtype=int64)
    return prime_sum, primes

t_start = time()
print('\33[32m', 'Sum of all primes below {} = {}'.format(n, sum_primes2(n)[0]), '\33[0m', sep="")
#print('\33[32m', 'List of all primes below {} = {}'.format(n, sum_primes2(n)[1]), '\33[0m', sep="")
print('\33[91;1m', "runtime = ", str(time() - t_start)[0:6], "s", '\33[0m', sep="")