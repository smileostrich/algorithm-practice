import sys
sys.setrecursionlimit(100000)
def dfs(v, group):
    li_visited[v] = group
    for i in dic_adj[v]:
        if li_visited[i] == 0:
            if dfs(i,-group) == False:
                return False
        elif li_visited[i] == li_visited[v]:
            return False
    return True


T = int(input())
for _ in range(T):
    V,E = map(int, sys.stdin.readline().split())
    dic_adj = {i:[] for i in range(1,V+1)}
    li_visited = [0]*(V+1)
    for _ in range(E):
        a,b = map(int, sys.stdin.readline().split())
        dic_adj[b].append(a)
        dic_adj[a].append(b)
    for i in range(1, V+1):
        if li_visited[i] == 0:
            chk = dfs(i, 1)
            if chk == False:
                break
    print('YES' if chk else 'NO')