# DP
# 54분

import sys
import copy

T = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(T)]

temp_n = copy.deepcopy(n)
temp_n.sort(reverse=True)
l = temp_n[0] + 1
# li = [0] * l
li_0 = [0] * l
li_1 = [0] * l

li_0[0], li_1[1] = 1, 1

for i in range(2, l):
    # li[i] = li[i-1] + li[i-2]
    li_0[i] = li_0[i-1] + li_0[i-2]
    li_1[i] = li_1[i-1] + li_1[i-2]

for i in n:
    print(str(li_0[i]) + " " + str(li_1[i]))