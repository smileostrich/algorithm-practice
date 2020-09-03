# 위상정렬이려면 dag 이어야함 (= 사이클이 없어야함)
# dfs로 구현 (order 리스트 만들어서 dfs 후 reverse)
vertexList = ['a', 'b', 'c', 'd', 'e']
edgeList = [('a', 'd'), ('b', 'd'), ('d', 'e'), ('c', 'e')]

# 시작
adjList = {i:[] for i in vertexList}
for v1, v2 in edgeList:
    adjList[v1].append(v2)

parent = {}
topological_order = []
def dfs_visit(adjList, s):
    for neighbor in adjList[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            dfs_visit(adjList, neighbor)
    topological_order.append(s)


def dfs(vList, adjList):
    for s in vList:
        if s not in parent:
            parent[s] = None
            dfs_visit(adjList, s)


dfs(vertexList, adjList)
topological_order.reverse()
print(topological_order)
