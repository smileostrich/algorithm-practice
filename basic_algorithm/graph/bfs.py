def BFS(s, adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1

# deque
# from collections import deque
#
#
# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
# root_node = 1
#
# def BFS_with_adj_list(graph, root):
#     visited = []
#     queue = deque([root])
#
#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             queue += graph[n] - set(visited)
#     return visited
#
#
# print(BFS_with_adj_list(graph_list, root_node))

# queue
# vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
# graphs = (vertexList, edgeList)
#
#
# def bfs(graph, start):
#     vertexList, edgeList = graph
#     visitedList = []
#     queue = [start]
#     adjacencyList = [[] for _ in vertexList]
#
#     for edge in edgeList:
#         adjacencyList[edge[0]].append(edge[1])
#
#     while queue:
#         current = queue.pop(0)
#         for neighbor in adjacencyList[current]:
#             if neighbor not in visitedList:
#                 queue.append(neighbor)
#         visitedList.append(current)
#     return visitedList
#
# print(bfs(graphs, 0))
