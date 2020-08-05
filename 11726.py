# dp 16분 소요
import sys

n = int(sys.stdin.readline())
li = [0]*(n+1)

if n == 1:
    li[1] = 1
else:
    li[1] = 1
    li[2] = 2
    for i in range(3, n+1):
        li[i] = li[i-1] + li[i-2]

print(li[n]%10007)