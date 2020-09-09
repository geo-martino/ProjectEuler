# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

sumsq = 0
totsq = 0
a = 100

for i in range(1, a+1):
    sumsq += i**2

for i in range(1, a+1):
    totsq += i

totsq **= 2
print(totsq-sumsq)
