from time import time
from math import factorial


# from numpy import sum, int64


# 14. Which starting number, under one million, produces the longest chain?

def prob14():
    t_start = time()

    i = 1
    i_max = 0
    n_values = []
    for n in range(2, 1000000):
        n_current = n
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                i += 1
            else:
                n = 3 * n + 1
                i += 1
            """
            if n in n_values:
                n = 1
            else:
                n_values.append(n)
            """

        if i > i_max:
            i_max = i
            n_max = n_current

        i = 1

    print('\33[32m', 'Longest chain = {} ({})'.format(n_max, i_max), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


def prob14_2():
    t_start = time()

    def check(number):
        count = 0
        while (True):
            try:
                if (list[number] != 0 & number != 1):
                    return count + list[number]
            except:
                pass

            if number == 1:
                list[number] = count + list[number]
                return count + list[number]

            if number % 2 == 0:
                number = int(number / 2)
                count += 1
            else:
                number = number * 3 + 1
                count += 1

    n = 1000000
    list = [0] * n
    for i in range(1, n):
        list[i] = (check(i))

    print('\33[32m', 'Longest chain = {} ({})'.format(list.index(max(list))), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 15. How many routes are there through a 20×20 grid?

def prob15():
    t_start = time()

    size = 20
    routes = factorial(size * 2) // (factorial(size)) ** 2

    print('\33[32m', 'Routes in grid of size {} = {}'.format(size, routes), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 16. What is the sum of the digits of the number 2^1000?

def prob16():
    t_start = time()

    digits = 2 ** 1000
    sum = 0

    while digits > 9:
        sum += digits % 10
        digits //= 10
    sum += digits

    print('\33[32m', 'Sum of all digits in 2^1000 = {}'.format(sum), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 17. If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

def prob17():
    t_start = time()

    def counter(number):
        units = [(0, 0), (1, 3), (2, 3), (3, 5), (4, 4), (5, 4), (6, 3), (7, 5), (8, 5), (9, 4)]
        teens = [(0, 3), (1, 6), (2, 6), (3, 8), (4, 8), (5, 7), (6, 7), (7, 9), (8, 8), (9, 8)]
        tenths = [(0, 0), (1, 3), (2, 6), (3, 6), (4, 5), (5, 5), (6, 5), (7, 7), (8, 6), (9, 6)]

        def hundreds(input):
            k = input // 100
            tenths_units = input % 100
            if tenths_units == 0:
                return units[input][1] + 7
            elif tenths_units < 20 and tenths_units >= 10:
                return teens[tenths_units % 10][1] + units[k][1] + 10
            else:
                return units[(tenths_units) % 10][1] + tenths[(tenths_units) // 10][1] + units[k][1] + 10

        letters = 0

        if number < 10:
            letters = units[number][1]
        elif number < 20:
            number %= 10
            letters = teens[number][1]
        elif number < 100:
            letters = units[number % 10][1] + tenths[number // 10][1]
        elif number < 1000:
            letters = hundreds(number)
        elif number <= 1000:
            number //= 1000
            letters += units[number][1] + 8

        print(number, letters)
        return letters

    n_max = 119
    sum = 0
    for i in range(n_max):
        sum += counter(i + 1)

    print('\33[32m', 'Sum of all letters in numbers < 1000 = {}'.format(sum), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


"""
print('\n', '\33[94;1m', "Problem 14 (v1):", '\33[0m')
prob14()
print('\n', '\33[94;1m', "Problem 14 (v2):", '\33[0m')
prob14_2()
print('\n', '\33[94;1m', "Problem 15:", '\33[0m')
prob15()
print('\n', '\33[94;1m', "Problem 16:", '\33[0m')
prob16()
"""
print('\n', '\33[94;1m', "Problem 17:", '\33[0m')
prob17()
