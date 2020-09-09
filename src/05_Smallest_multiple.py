# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

import time
tstart = time.time()

k = 1
i = 1

while k != 20:
    if i%k == 0:
        k += 1
    else:
        i += 1
        k = 1

print(i)
print ("runtime =", str(time.time() - tstart)[0:6],"seconds")