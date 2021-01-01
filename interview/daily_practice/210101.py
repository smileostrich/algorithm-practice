from collections import deque


vertexList = [1,2,3,4,5]
edgeList = [(1,2),(3,4),(4,5)]
adjList = {i:[] for i in vertexList}
for v1, v2 in edgeList:
    adjList[v1].append(v2)

parent = {}


def dfs(s):
    stack = [s]
    while stack:
        current = stack.pop()
        print(current, end=' ')
        for neighbor in adjList[current]:
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)


def bfs(s):
    queue = deque([s])
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for neighbor in adjList[current]:
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

# dfs(1)
bfs(1)