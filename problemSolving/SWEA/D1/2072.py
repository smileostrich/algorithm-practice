# 10분
from sys import stdin

inp = lambda : stdin.readline().rstrip()

for _ in range(int(inp())):
    t = (i for i in map(int, inp().split()) if i%2 == 1)
    print(sum(t))
