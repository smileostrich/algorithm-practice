# 위상정렬이려면 dag 이어야함 (= 사이클이 없어야함)
# dfs로 구현
vertexList = ['a', 'b', 'c', 'd', 'e']
edgeList = [('a', 'd'), ('b', 'd'), ('d', 'e'), ('c', 'e')]
adjList = {i:[] for i in vertexList}
for v1, v2 in edgeList:
    adjList[v1].append(v2)
print(adjList)

parent = {}
time = {}
def dfs(vList, adj, s):
    ft = 0
    for neighbor in adj[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            dfs(vList, adj, neighbor)
    ft += 1
    time[s] = ft

def dfs_v(vList, adj):
    parent = {}

    for s in vList:
        if s not in parent:
            parent[s] = None
            dfs(vList, adj, s)


dfs_v(vertexList, adjList)
print(parent, time)
