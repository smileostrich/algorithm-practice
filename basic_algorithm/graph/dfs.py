# 정점 s(시작점)가 없을때 모든 vertex들을 s로 설정하며 위상정렬, 사이클 유무 등 판단
vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]


# mit 소스 (위상정렬, 사이클 유무 문제풀때 편함)
parent = {s:None}
def dfs(vList, adj, s):
    for neighbor in adj[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            dfs(vList, adj, neighbor)


def dfs_v(vList, adj):
    parent = {}
    for current in vList:
        if current not in parent:
            parent[current] = None
            dfs_v(vList, adj, current)



# 일반적인 dfs 알고리즘
# graphs = (vertexList, edgeList)
# adjList = [[] for _ in vertexList]
# for edge in edgeList:
#     adjList[edge[0]].append(edge[1])

# def dfs(adjList, start):
#     visitedVertex = []
#     stack = [start]
#     while stack:
#         current = stack.pop()
#         for neighbor in adjList[current]:
#             if neighbor not in visitedVertex:
#                 stack.append(neighbor)
#         visitedVertex.append(current)
#     return visitedVertex

# print(dfs(adjList, 0))


# set 이용 무순서성 때문에 개인적으로 비 선호
# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
# root_node = 1
#
# def DFS_with_adj_list(graph, root):
#     visited = []
#     stack = [root]
#
#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             stack += graph[n] - set(visited)
#     return visited
#
# print(DFS_with_adj_list(graph_list, root_node))



