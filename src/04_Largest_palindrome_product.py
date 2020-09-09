# Find the largest palindrome made from the product of two 3-digit numbers

import time
tstart = time.time()

pd = 0
for i in range(100,1000):
    for j in range(i,1000):
        a = i*j
        digits = [int(a) for a in str(a)]
        digits_maxhalf = len(digits) // 2
        if digits == digits[::-1] and a > pd:
            pd = a

print (pd)
print ("runtime =", str(time.time() - tstart)[0:6],"seconds")