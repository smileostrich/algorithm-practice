def dfs_visit(s, level):
    for neighbor in adjList[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            levelDict[s] = level
            dfs_visit(neighbor, level)

def dfs():
    level = 0
    for s in vertexList:
        if s not in parent:
            parent[s] = None
            levelDict[s] = 0
            dfs_visit(s, level)
            level += 1
    return level


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li_tmp = list(map(int, input().split()))
    adjList = {i:[] for i in range(1,N+1)}
    vertexList = [i for i in range(1,N+1)]
    parent = {}
    levelDict = {}
    for i in range(0, len(li_tmp),2):
        adjList[li_tmp[i]].append(li_tmp[i+1])
        adjList[li_tmp[i+1]].append(li_tmp[i])
    dfs()
    cnt = 0
    for i in parent.values():
        if i == None:
           cnt += 1
    print(f'#{tc} {cnt}')