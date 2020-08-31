# 위상정렬이려면 dag 이어야함 (= 사이클이 없어야함)
# dfs로 구현
vertexList = ['a', 'b', 'c', 'd', 'e']
edgeList = [('a', 'd'), ('b', 'd'), ('d', 'e'), ('c', 'e')]
adjList = {i:[] for i in vertexList}
for v1, v2 in edgeList:
    adjList[v1].append(v2)


def dfs(adj, s):
    stack = [s]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        for neighbor in adj[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited

for
print(dfs(adjList, 'a'))