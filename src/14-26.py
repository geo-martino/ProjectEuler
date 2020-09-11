from math import factorial
from time import time


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
        units = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
        teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
        tenths = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

        def hundreds(input):
            hundreth = input // 100
            tenths_units = input % 100
            if tenths_units == 0:
                return units[hundreth] + 7
            elif tenths_units < 20 and tenths_units >= 10:
                return teens[tenths_units % 10] + units[hundreth] + 10
            else:
                return units[(tenths_units) % 10] + tenths[(tenths_units) // 10] + units[hundreth] + 10

        letters = 0

        if number < 10:
            letters = units[number]
        elif number < 20:
            number %= 10
            letters = teens[number]
        elif number < 100:
            letters = units[number % 10] + tenths[number // 10]
        elif number < 1000:
            letters = hundreds(number)
        elif number == 1000:
            number //= 1000
            letters += units[number] + 8

        return letters

    n_max = 1000
    sum = 0
    for i in range(n_max):
        sum += counter(i + 1)

    print('\33[32m', 'Sum of all letters in numbers < {} = {}'.format(n_max, sum), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 18. Find the maximum total from top to bottom of the triangle below:

def prob18():
    t_start = time()

    numbers = [[75],
               [95, 64],
               [17, 47, 82],
               [18, 35, 87, 10],
               [20, 4, 82, 47, 65],
               [19, 1, 23, 75, 3, 34],
               [88, 2, 77, 73, 7, 63, 67],
               [99, 65, 4, 28, 6, 16, 70, 92],
               [41, 41, 26, 56, 83, 40, 80, 70, 33],
               [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
               [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
               [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
               [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
               [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
               [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

    for i in range(len(numbers) - 1, 0, -1):
        added = []
        for j in range(0, len(numbers[i]) - 1):
            added.append(numbers[i - 1][j] + max(numbers[i][j], numbers[i][j + 1]))
        numbers.remove(numbers[i])
        numbers[i - 1] = added

    print('\33[32m', 'Maximum total = {}'.format(numbers[0][0]), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 19. How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def prob19():
    t_start = time()

    day = 2
    month = 1
    year = 1901
    count = 0

    while year < 2001:
        if day == 0:
            count += 1

        if month == 12:
            day = (day + 31) % 7
            month = 0
            year += 1
        elif month in (1, 3, 5, 7, 8, 10):
            day = (day + 31) % 7
        elif month in (4, 6, 9, 11):
            day = (day + 30) % 7
        elif month == 2 and year % 4 == 0:
            day = (day + 29) % 7
        # elif month == 2 and year % 4 != 0:
        #    continue
        month += 1

    print('\33[32m', 'Total Sundays in 20th Century = {}'.format(count), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 20.  Find the sum of the digits in the number 100!

def prob20():
    t_start = time()

    def factorial(n):
        fact = n
        for i in range(n):
            fact *= n - i
        return fact


    def digits_sum(digits):
        sum = 0
        while digits > 9:
            sum += digits % 10
            digits //= 10
        sum += digits
        return sum

    n = 100

    print('\33[32m', 'Sum of all digits in {}! = {}'.format(n, digits_sum(factorial(n))), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 21.

def prob21():
    t_start = time()

"""
print('\n', '\33[94;1m', "Problem 14 (v1):", '\33[0m')
prob14()
print('\n', '\33[94;1m', "Problem 14 (v2):", '\33[0m')
prob14_2()
print('\n', '\33[94;1m', "Problem 15:", '\33[0m')
prob15()
print('\n', '\33[94;1m', "Problem 16:", '\33[0m')
prob16()
print('\n', '\33[94;1m', "Problem 17:", '\33[0m')
prob17()
print('\n', '\33[94;1m', "Problem 18:", '\33[0m')
prob18()
print('\n', '\33[94;1m', "Problem 19:", '\33[0m')
prob19()
print('\n', '\33[94;1m', "Problem 20:", '\33[0m')
prob20()
"""
print('\n', '\33[94;1m', "Problem 21:", '\33[0m')
prob21()
