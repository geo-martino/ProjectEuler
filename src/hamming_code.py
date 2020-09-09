# Version 1
# design a 16-bit hamming code check.

from functools import reduce
from operator import xor
from time import time

import numpy as np

print('\33[94;1m', "16 bits", '\33[0m')

t_start = time()

check = [[0, 0, 1, 1],
         [0, 0, 1, 1],
         [1, 0, 0, 1],
         [0, 1, 1, 0]]


def hamming_check(code):
    """
    :param code: 16-bit binary list
    :return: # of detected errors or corrected bits if only 1 error
    """
    col_sum = np.sum(code, axis=0)
    row_sum = np.sum(code, axis=1)
    col_len = len(col_sum) - 1
    row_len = len(row_sum) - 1

    error = np.sum(code)
    hamming = []
    position = 0

    for i in range(1, col_len):
        hamming.append((col_sum[i] + col_sum[col_len]) % 2)
    for i in range(1, row_len):
        hamming.append((row_sum[i] + row_sum[row_len]) % 2)

    for i in range(len(hamming)):
        position += hamming[i] * 2 ** i

    if error % 2 == 0 and position == 0:
        print('\33[32m', 'no error detected', '\33[0m', sep="")
        return
    elif error % 2 == 0 and position > 0:
        print('\33[91;1m', 'at least 2 errors detected', '\33[0m', sep="")
        return

    x = position // 4
    y = position % 4
    print('\33[91;1m', 'at least 1 error detected', '\33[0m', sep="")
    print('error detected at position [{}][{}]'.format(x, y))

    if code[x][y] == 0:
        code[x][y] = 1
    else:
        code[x][y] = 0
    print('\33[32m', 'corrected bits = {} '.format(code), '\33[0m', sep="")
    return


print('input bits = {} '.format(check))
hamming_check(check)
print('\33[91;1m', "runtime = ", str(time() - t_start)[0:6], "s", '\33[0m', sep="")

# Version 2
# design a hamming code check for any 2^n bits.

print('\n', '\33[94;1m', "Any 2^n bits", '\33[0m')

t_start = time()

bits16 = [[0, 0, 1, 1],
          [0, 1, 1, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]]

bits = np.random.randint(0, 2, 64)


def one_d_array(input_bits):
    """
    :param input_bits: any 2^n bit binary 2d array
    :return: 2^n bit binary list
    """
    bits = []
    for i in range(len(input_bits[0])):
        for j in range(len(input_bits[0])):
            bits.append(input_bits[i][j])
    return bits


def hamming_check(bits: list):
    """
    :param bits: any 2^n bit binary list
    :return: # of detected errors or corrected bits if only 1 error
    """
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
