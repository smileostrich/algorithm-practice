# 정점 s(시작점)가 없을때 모든 vertex들을 s로 설정하며 위상정렬, 사이클 유무 등 판단
vertexList = [0,1,2,3,4,5,6]
edgeList = [(0,1), (0,2), (1,0), (1,3), (2,0), (2,4), (2,5), (3,1), (4,2), (4,6), (5,2), (6,4)]


adjList = {i:[] for i in vertexList}
for v1, v2 in edgeList:
    adjList[v1].append(v2)
parent = {}


# 재귀 사용해서 만듬 (위상정렬, 사이클 유무 문제풀때 편함)
# 주의 사항 : adjList 만들때 i string/int 여부 확인 string --> int 변환 실수 조심

def dfs_visit(adjList, s):
    for neighbor in adjList[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            dfs_visit(adjList, neighbor)


def dfs(vList, adjList):
    for s in vList:
        if s not in parent:
            parent[s] = None
            dfs_visit(adjList, s)


dfs(vertexList, adjList)
print(parent)

# 이 아래 소스들은 전부 방문 즉시 종료[= dfs와 bfs 혼합] 즉, 사용하면 안됨
############################################################################
# 이 소스 사용 x 비재귀 parent (방문 즉시 종료[= 처음들어간게 제일먼저 끝남])
# def dfs_visit(adjList, s):
#     stack = [s]
#     while stack:
#         current = stack.pop()
#         for neighbor in adjList[current]:
#             if neighbor not in parent:
#                 parent[neighbor] = current
#                 stack.append(neighbor)
#
#
# def dfs(adjList, vList):
#     for s in vList:
#         if s not in parent:
#             parent[s] = None
#             dfs_visit(adjList, s)
#
#
# dfs(adjList, vertexList)
# print(parent)


# 비재귀 dfs with visitedList
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



