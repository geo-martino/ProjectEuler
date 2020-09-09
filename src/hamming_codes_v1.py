# design a 16-bit hamming code check.

from time import time
import numpy as np

t_start = time()

check = [[0, 0, 1, 1],
         [0, 0, 1, 1],
         [1, 0, 0, 1],
         [0, 1, 1, 0]]


def hamming_check(code):
    col_sum = np.sum(code, axis=0)
    row_sum = np.sum(code, axis=1)
    col_len = len(col_sum) - 1
    row_len = len(row_sum) - 1

    error = np.sum(code)
    hamming = []
    position = 0

    for i in range(1, col_len):
        hamming.append((col_sum[i]+col_sum[col_len]) % 2)
    for i in range(1, row_len):
        hamming.append((row_sum[i]+row_sum[row_len]) % 2)

    for i in range(len(hamming)):
        position += hamming[i] * 2**i

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
    print('\33[32m', 'corrected hamming code = {} '.format(code), '\33[0m', sep="")
    return


print('input hamming code = {} '.format(check))
hamming_check(check)
print('\33[91;1m', "runtime = ", str(time() - t_start)[0:6], "s", '\33[0m', sep="")
