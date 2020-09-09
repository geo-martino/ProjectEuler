# What is the 10001st prime number?
import time, math

t_start = time.time()


def is_prime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if not n % j:
            return False
    return True


i = 1
i_max = 10001
num = 2

while i != i_max + 1:
    if is_prime(num):
        i += 1
        if i != i_max + 1:
            num += 1
    if not is_prime(num):
        num += 1

print('\33[32m', i_max, "st prime is ", num, '\33[0m', sep="")
print('\33[91;1m', "runtime = ", str(time.time() - t_start)[0:6], "s", '\33[0m', sep="")
