# 사소한 실수로 10분 지체
# dfs 알고리즘 바꿔서 10분 지체
# 38분 1차. 디버깅시작
# dfs


# import sys
# testcase = int(sys.stdin.readline().rstrip())
# for _ in range(testcase):
#     n = int(sys.stdin.readline().rstrip())
#     choice = [0] + list(map(int, sys.stdin.readline().split()))
#     visit = [0] * (n+1)
#     group = 1
#     for i in range(1, n+1):
#         if visit[i] == 0:
#             while visit[i] == 0:
#                 visit[i] = group
#                 i = choice[i]
#             while visit[i] == group:
#                 visit[i] = -1
#                 i = choice[i]
#             group += 1
#     cnt = 0
#     for v in visit:
#         if v > 0:
#             cnt += 1
#     print(f'{cnt}')


# import sys
#
# n = int(sys.stdin.readline().rstrip())
# choice = [0] + list(map(int, sys.stdin.readline().split()))
# visit = [0] * (n+1)
# group = 1
# for i in range(1, n+1):
#     if visit[i] == 0:
#         while visit[i] == 0:
#             visit[i] = group
#             i = choice[i]
#         while visit[i] == group:
#             visit[i] = -1
#             i = choice[i]
#         group += 1
# cnt = 0
# for v in visit:
#     if v > 0:
#         cnt += 1
# print(f'{cnt}')


# import sys
# sys.setrecursionlimit(1000000)
# T = int(sys.stdin.readline().rstrip())
# for _ in range(T):
#     n = int(sys.stdin.readline().rstrip())
#
#     adjList = dict(map(lambda x: (x[0]+1,[int(x[1])]), enumerate(sys.stdin.readline().split())))
#     parent = {}
#     levelDict = {}
#     def dfs_visit(s, level):
#         for neighbor in adjList[s]:
#             if neighbor not in parent:
#                 parent[neighbor] = s
#                 levelDict[neighbor] = level
#                 dfs_visit(neighbor, level)
#             if levelDict[neighbor] == level:
#                 levelDict[neighbor] = -1
#                 dfs_visit(neighbor, level)
#
#
#     def dfs():
#         level = 0
#         for s in range(1,n+1):
#             if s not in parent:
#                 level += 1
#                 parent[s] = None
#                 levelDict[s] = level
#                 dfs_visit(s, level)
#
#         cnt = 0
#         for v in levelDict.values():
#             if v != -1:
#                 cnt += 1
#         return cnt
#     print(dfs())


import sys
sys.setrecursionlimit(1000000)
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    adjList = dict(map(lambda x: (x[0]+1,[int(x[1])]), enumerate(sys.stdin.readline().split())))
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

    vertexList = [i for i in range(1, n+1)]
    dfs(vertexList, adjList)
    topological_order.reverse()
    print(topological_order)


# parent = {i: None for i in range(1, n+1)}
# for s in range(1, n+1):
#     if parent[s] == 0:
#         for neighbor in adjList[s]:
#             if neighbor not in parent:
#                 parent[neighbor] = s
#                 dfs_visit(neighbor)
