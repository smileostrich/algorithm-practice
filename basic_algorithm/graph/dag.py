# dfs로 구현
# dag판별(사실상 example graph는 dag x)
# dag유무 및 사이클 갯수(단, 사이클이 연결되어 있을 수 있음)

vertexList = ['a', 'b', 'c', 'd', 'e', 'f']
edgeList = [('a', 'b'), ('b', 'e'), ('e', 'd'), ('d', 'b'), ('a', 'd'), ('c', 'f'), ('f', 'f'), ('c', 'e')]

adjList = {i:[] for i in vertexList}
for v1, v2 in edgeList:
    adjList[v1].append(v2)

parent = {}
cycleList = []
cycleCnt = []
def dfs_visit(adjList, s):
    for neighbor in adjList[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            dfs_visit(adjList, neighbor)
        elif len(cycleCnt):
            cycleList.append([cycleList[-1] + [s]])
        else:
            cycleCnt.append(1)
            cycleList.append(neighbor)
            count_cycle(s)


# cycle 갯수(떨어져 있는것만)
def count_cycle(s):
    cycleList.append(s)
    if parent[s] not in cycleList:
        count_cycle(parent[s])


def dfs(vList, adjList):
    for s in vList:
        if s not in parent:
            parent[s] = None
            dfs_visit(adjList, s)


dfs(vertexList, adjList)
print(cycleList)