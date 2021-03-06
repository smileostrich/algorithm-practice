def minKey(weight, mstSet):
    low = 2147483647
    low_index = 0
    for v in range(V+1):
        if mstSet[v] == 0 and (weight[v] < low):
            low = weight[v]
            low_index = v
    return low_index


def printMST(parent):
    weightSum = 0
    for i in range(1, V+1):
        weightSum += dic_graph[i][parent[i]]
    print(weightSum)


def primMST():
    parent = [0] * (V+1)
    weight = [2147483647] * (V+1)
    mstSet = [0] * (V+1)
    weight[0] = 0
    parent[0] = -1
    for _ in range(0, V+1):
        u = minKey(weight, mstSet)
        mstSet[u] = 1
        for v in range(0, V+1):
            if v in dic_graph[u] and mstSet[v] == 0 and dic_graph[u][v] < weight[v]:
                parent[v] = u
                weight[v] = dic_graph[u][v]
    printMST(parent)

T = int(input())
for tc in range(1, T+1):
    V, M = map(int, input().split())
    dic_graph = {v:{} for v in range(V+1)}
    for _ in range(M):
        v1,v2,w = map(int, input().split())
        dic_graph[v1][v2] = w
        dic_graph[v2][v1] = w
    print(f'#{tc}', end= ' ')
    primMST()

# V,E = map(int,input().split())
# INF = 0xfffffff
# adj = [[INF]*V for _ in range(V)]
# for i in range(E):
#     s,e,w = map(int,input().split())
#     adj[s][e] = w
#     adj[e][s] = w
#
# def prim(start):
#     INF = 0xfffffff
#     weight = [INF]*V
#     weight[start] = 0
#     mst = [0] * V
#     result = 0
#     st = [-1] * V
#     for _ in range(V):
#         print(weight)
#         min_w = 0xffffff
#         min_v = 0
#         for i in range(V):
#             if mst[i] == 0 and weight[i] < min_w:
#                 min_w = weight[i]
#                 min_v = i
#         mst[min_v] = 1
#         result += min_w
#         for i in range(V):
#             if adj[min_v][i] < weight[i] and mst[i]==0:
#                 weight[i] = adj[min_v][i]
#                 st[i] = min_v
#     return result
#
# result=prim(0)
# print(result)