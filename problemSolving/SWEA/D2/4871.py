from collections import deque

def bfs(s):
    visited = []
    d = deque([s])
    while d:
        cur = d.popleft()
        for neighbor in adjList[cur]:
            if neighbor not in visited:
                d.append(neighbor)
        visited.append(cur)
    return visited

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjList = {i:[] for i in range(1,V+1)}
    for _ in range(E):
        f, t = map(int, input().split())
        adjList[f].append(t)
    S,G = map(int, input().split())
    if G in bfs(S):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')