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

    print(list.index(max(list)))
    print('\33[91;1m', "runtime = ", str(time() - t_start), "s", '\33[0m', sep="")


print('\n', '\33[94;1m', "Problem 14 (v1):", '\33[0m')
prob14()
print('\n', '\33[94;1m', "Problem 14 (v2):", '\33[0m')
prob14_2()
