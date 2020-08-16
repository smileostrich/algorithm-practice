graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(DFS_with_adj_list(graph_list, root_node))


# vertexList = ['0', '1', '2', '3', '4', '5', '6']
# edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
# graphs = (vertexList, edgeList)
#
#
# def dfs(graph, start):
#     vertexList, edgeList = graph
#     visitedVertex = []
#     stack = [start]
#     adjacencyList = [[] for _ in vertexList]
#
#     for edge in edgeList:
#         adjacencyList[edge[0]].append(edge[1])
#
#     while stack:
#         current = stack.pop()
#         for neighbor in adjacencyList[current]:
#             if neighbor not in visitedVertex:
#                 stack.append(neighbor)
#         visitedVertex.append(current)
#     return visitedVertex
#
#
# print(dfs(graphs, 0))
