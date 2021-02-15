import sys
import re

T = int(1)
for test_case in range(1, T + 1):
    # N = int(input())
    N = 1
    high = 0
    # for i in range(100):
    #     for j in range(100):
    for i in range(1, 5+1):
        row = 0
        for j in range(1, 5+1):
            row += j
        if row > high:
            high = row
    for k in range(5):
