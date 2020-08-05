import sys
import copy

T = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(T)]
t = copy.deepcopy(n)
t.sort(reverse=True)
li = [0]*(t[0]+1)

for i in range(1, t[0]+1):
    if i == 1:
        li[i] = 1
    elif i == 2:
        li[i] = 2
    elif i == 3:
        li[i] = 4
    else:
        li[i] = li[i-3] + li[i-2] + li[i-1]

for i in n:
    print(li[i])