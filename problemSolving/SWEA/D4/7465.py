def dfs_visit(s, level):
    for neighbor in dic_adj[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            dic_level[s] = level
            dfs_visit(neighbor, level)
def dfs():
    level = 0
    for s in range(1,N+1):
        if s not in parent:
            parent[s] = None
            dic_level[s] = 0
            dfs_visit(s,level)
            level += 1
    return level

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    dic_adj = {i:[] for i in range(1,N+1)}
    parent = {}
    dic_level = {}
    for _ in range(M):
        a,b = map(int, input().split())
        dic_adj[a].append(b)
        dic_adj[b].append(a)
    print(f'#{tc} {dfs()}')