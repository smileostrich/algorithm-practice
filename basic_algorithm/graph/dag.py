# dfs로 구현


vertexList = ['a', 'b', 'c']
edgeList = [('a', 'b'), ('b', 'c'), ('c', 'a')]
adjList = {i:[] for i in vertexList}
for v1, v2 in edgeList:
    adjList[v1].append(v2)
print(adjList)

parent = {'a': None}
cCount = 0

def dfs(adj, sV, ):
    for neighbor in adj[sV]:
        print(neighbor)
        if neighbor not in parent:
            parent[neighbor] = sV
            dfs(adj, neighbor)
        elif neighbor in parent:
            print("cycle exist")
            cCount += 1

dfs(adjList, 'a')
print(parent)


# def dfs_v(vList, adj):
#     parent = {}
#
#     for s in vList:
#         if s not in parent:
#             parent[s] = None
#             dfs(vList, adj, s)

# dfs_v(vertexList, adjList)
# print(parent, time)
