# design a hamming code check for any 2^n bits.

from time import time
import numpy as np
from functools import reduce
from operator import xor

t_start = time()

bits16 = [[0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]]

bits = np.random.randint(0, 2, 64)

def one_d_array(input_bits):
    bits = []
    for i in range(len(input_bits[0])):
        for j in range(len(input_bits[0])):
            bits.append(input_bits[i][j])
    return bits

def hamming_check(bits):
    ones = [i for i, bit in enumerate(bits) if bit]
    position = reduce(xor, ones)
    error = np.sum(bits)

    if error % 2 == 0 and position == 0:
        print('\33[32m', 'no error detected', '\33[0m', sep="")
        return
    elif error % 2 == 0 and position > 0:
        print('\33[91;1m', 'at least 2 errors detected', '\33[0m', sep="")
        return

    print('\33[91;1m', 'error detected at position {}'.format(position), '\33[0m', sep="")

    if bits[position] == 0:
        bits[position] = 1
    else:
        bits[position] = 0
    print('\33[32m', 'corrected bits = {} '.format(bits), '\33[0m', sep="")
    return


print('input bits = {} '.format(bits))
hamming_check(bits)
print('\33[91;1m', "runtime = ", str(time() - t_start)[0:6], "s", '\33[0m', sep="")
