# Find the sum of the even-valued fibonacci numbers

numbers,n = 0
n,i,j = 0,1,1
while n + i < 4000000:
    n += i
    if n%2 == 0:
        numbers += n
    i,j = j,n

print(numbers)