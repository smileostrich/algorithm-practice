import sys

n = int(sys.stdin.readline())
k = list(sys.stdin.readline())
a = 0

for i in range(n):
    a += int(k[i])

print(a)