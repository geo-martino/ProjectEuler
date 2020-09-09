# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family

def primetest(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i += 1
    print(n)

primetest(68765)