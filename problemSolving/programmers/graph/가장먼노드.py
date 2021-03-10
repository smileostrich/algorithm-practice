# 10분

def bfs(s, adj):
    frontier = [s]
    level = {s:0}
    i = 1
    while frontier:
        next = []
        for cur in frontier:
            for neighbor in adj[cur]:
                if neighbor not in level:
                    level[neighbor] = i
                    next.append(neighbor)
        frontier = next
        i += 1
    return level

def solution(n, edge):
    dic_adj = {}
    for a,b in edge:
        if a not in dic_adj:
            dic_adj[a] = [b]
        else:
            dic_adj[a].append(b)
        if b not in dic_adj:
            dic_adj[b] = [a]
        else:
            dic_adj[b].append(a)
    level = bfs(1,dic_adj)
    high = max(level.values())
    cnt = 0
    for i in level.values():
        if i == high:
            cnt += 1
    return cnt