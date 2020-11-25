from sys import stdin
from collections import deque


N, M = map(int, stdin.readline().rstrip().split())
mat = [[0]*N for _ in range(N)]

for i in range(N):
    mat[i] = list(map(int, stdin.readline().rstrip().split()))


def bfs(s):
    q = deque
    q.append(s)

    while q:
        for i in

print(mat)