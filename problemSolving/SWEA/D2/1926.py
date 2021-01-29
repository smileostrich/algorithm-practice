import sys
import re

T = int(1)
for test_case in range(1, T + 1):
    x = str(x)
    sum = 0
    sum += x.count('3')
    sum += x.count('6')
    sum += x.count('9')
    if sum != 0:
        print('-' * sum, end=' ')
    else:
        print(x, end=' ')