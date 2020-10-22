import sys
import math

dat = {1:[1], 2:[10, 2,4,6,8], 3:[1, 3,9,7], 4:[6,4], 5:[5], 6:[6], 7:[1,7,9,3], 8:[6,8,4,2], 9:[1,9], 0:[0]}
print()
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    num = int(str(a)[-1])
    k = len(dat[num])
    re = dat[num][b % k]
    print(re)


