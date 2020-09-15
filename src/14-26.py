from math import factorial
from time import time


# from numpy import sum, int64


# 14. Which starting number, under one million, produces the longest chain?


def p14():
    t_start = time()

    i = 1
    i_max, n_max = 0, 0
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


def p14_2():
    t_start = time()

    def check(number):
        count = 0
        while True:
            try:
                if n_list[number] != 0 & number != 1:
                    return count + n_list[number]
            except IndexError:
                pass

            if number == 1:
                n_list[number] = count + n_list[number]
                return count + n_list[number]

            if number % 2 == 0:
                number = int(number / 2)
                count += 1
            else:
                number = number * 3 + 1
                count += 1

    n = 1000000
    n_list = [0] * n
    for i in range(1, n):
        n_list[i] = (check(i))

    print('\33[32m', 'Longest chain = {}'.format(n_list.index(max(n_list))), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 15. How many routes are there through a 20×20 grid?

def p15():
    t_start = time()

    size = 20
    routes = factorial(size * 2) // (factorial(size)) ** 2

    print('\33[32m', 'Routes in grid of size {} = {}'.format(size, routes), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 16. What is the sum of the digits of the number 2^1000?

def p16():
    t_start = time()

    digits = 2 ** 1000
    digits_sum = 0

    while digits > 9:
        digits_sum += digits % 10
        digits //= 10
    digits_sum += digits

    print('\33[32m', 'Sum of all digits in 2^1000 = {}'.format(digits_sum), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 17. If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

def p17():
    t_start = time()

    def counter(number):
        units = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
        teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
        tenths = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

        def hundreds(j):
            hundredth = j // 100
            tenths_units = j % 100
            if tenths_units == 0:
                return units[hundredth] + 7
            elif 20 > tenths_units >= 10:
                return teens[tenths_units % 10] + units[hundredth] + 10
            else:
                return units[tenths_units % 10] + tenths[tenths_units // 10] + units[hundredth] + 10

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
    n_sum = 0
    for i in range(n_max):
        n_sum += counter(i + 1)

    print('\33[32m', 'Sum of all letters in numbers < {} = {}'.format(n_max, n_sum), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 18. Find the maximum total from top to bottom of the triangle below:

def p18():
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

def p19():
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

def p20():
    t_start = time()

    def my_factorial(i):
        fact = i
        for i in range(i):
            fact *= i - i
        return fact

    def digits_sum(digits):
        total = 0
        while digits > 9:
            total += digits % 10
            digits //= 10
        total += digits
        return total

    n = 100

    print('\33[32m', 'Sum of all digits in {}! = {}'.format(n, digits_sum(my_factorial(n))), '\33[0m', sep="")
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


# 21.  Evaluate the sum of all the amicable numbers under 10000.

def p21():
    t_start = time()

    def factor_sum(k):
        factor_tot = 1
        max = int(k ** 0.5)
        for j in range(2, max):
            if k % j == 0:
                factor_tot += j + (k // j)

        return factor_tot

    n = 10000
    attempt = [0] * n
    total = 0

    for i in range(4, n):
        fsum = factor_sum(i)
        if i == factor_sum(fsum) and i != fsum:
            attempt[i] = 1
            attempt[fsum] = 1
        else:
            attempt[i] = 2

    for i in range(n):
        if attempt[i] == 1:
            total += i
            print(i, "--", factor_sum(i))

    print('\33[32m', 'Sum of all amicable numbers <{} = {}'.format(n, total), '\33[0m', sep="")
    print('\33[91;1m', 'runtime = {}'.format(str(time() - t_start)), "s", '\33[0m', sep="")


# 22. What is the total of all the name scores in the file?

def p22():
    t_start = time()
    """
    def merge(left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left

        result = []
        index_left = index_right = 0

        while len(result) < len(left) + len(right):
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            if index_right == len(right):
                result += left[index_left:]
                break

            if index_left == len(left):
                result += right[index_right:]
                break

        return result

    def mergesort(array):
        if len(array) < 2:
            return array

        mid = len(array) // 2
        return merge(left = mergesort(array[:mid]), right = mergesort(array[mid:]))
    """

    with open('D:\Coding\ProjectEuler\\resources\p022_names.txt', 'r') as file:
        names = sorted(file.read().replace('"', "").split(','))

    total = 0
    for i in range(len(names)):
        total += sum([ord(names[i][j]) - ord('A') + 1 for j in range(len(names[i]))]) * (i + 1)

    print('\33[32m', 'Sum of all names scores  = {}'.format(total), '\33[0m', sep="")
    print('\33[91;1m', 'runtime = {}'.format(str(time() - t_start)), "s", '\33[0m', sep="")


# 23. Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def p23():
    t_start = time()

    def factor_sum(n):
        factors = [1]
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                factors.extend([j, n // j])

        return sum(list(set(factors)))

    upper = 28123
    ab = []
    total = list(range(upper))

    for i in range(12, upper):
        test = factor_sum(i)
        if test > i:
            ab.append(i)

    for j in range(len(ab)):
        for k in range(j, len(ab)):
            if ab[j] + ab[k] < upper:
                total[ab[j] + ab[k]] = 0
            else:
                break

    print('\33[32m', 'Sum = {}'.format(sum(total)), '\33[0m', sep="")
    print('\33[91;1m', 'runtime = {}'.format(str(time() - t_start)), "s", '\33[0m', sep="")

# 24. What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def p24():
    t_start = time()


"""
print('\n', '\33[94;1m', "Problem 14 (v1):", '\33[0m')
p14()
print('\n', '\33[94;1m', "Problem 14 (v2):", '\33[0m')
p14_2()
print('\n', '\33[94;1m', "Problem 15:", '\33[0m')
p15()
print('\n', '\33[94;1m', "Problem 16:", '\33[0m')
p16()
print('\n', '\33[94;1m', "Problem 17:", '\33[0m')
p17()
print('\n', '\33[94;1m', "Problem 18:", '\33[0m')
p18()
print('\n', '\33[94;1m', "Problem 19:", '\33[0m')
p19()
print('\n', '\33[94;1m', "Problem 20:", '\33[0m')
p20()
print('\n', '\33[94;1m', "Problem 21:", '\33[0m')
p21()
print('\n', '\33[94;1m', "Problem 22:", '\33[0m')
p22()
print('\n', '\33[94;1m', "Problem 23:", '\33[0m')
p23()
"""
print('\n', '\33[94;1m', "Problem 24:", '\33[0m')
p24()
