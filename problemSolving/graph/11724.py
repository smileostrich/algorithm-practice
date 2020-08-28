import sys


N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)


def BFS(s, adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    print(i, parent, level)


for i in range(1, N+1):
    BFS(i, adj)


