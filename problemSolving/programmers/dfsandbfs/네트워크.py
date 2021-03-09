# 30분

def dfs(s, dic_adj):
    stack = [s]
    visited = []
    while stack:
        cur = stack.pop()
        for neighbor in dic_adj[cur]:
            if neighbor not in visited:
                stack.append(neighbor)
        visited.append(cur)
    return visited


def solution(n, computers):
    dic_adj = {i: [] for i in range(n)}
    li_re = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                dic_adj[i].append(j)
                dic_adj[j].append(i)
    for i in range(n):
        if i not in li_re:
            cnt += 1
            li_re.extend(dfs(i, dic_adj))
    return cnt

