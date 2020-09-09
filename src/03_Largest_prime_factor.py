# What is the largest prime factor of the number 600851475143
import time

tstart = time.time()

n = 876589
prime = 0

for i in range(2, n):
    sum = 0
    if n % i == 0:
        for j in range(1, i):
            if i % j == 0:
                sum += j
    if sum == 1:
        prime = i

print("largest prime = ", prime)
print("runtime =", str(time.time() - tstart)[0:6], "seconds")

tstart = time.time()

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i += 1
print(n)
print("runtime =", str(time.time() - tstart)[0:6], "seconds")
