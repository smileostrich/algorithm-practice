# 45분
import sys


N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
area = [0]*(N+1)
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)


def dfs(s, adj):
    stack = [s]
    while stack:
        current = stack.pop()
        if area[current] != 1:
            area[current] = 1
            for neighbor in adj[current]:
                if area[neighbor] != 1:
                    stack.append(neighbor)
    return 1

cnt = 0
for i in range(1, N+1):
    if area[i] == 0:
        cnt += dfs(i, adj)

print(cnt)