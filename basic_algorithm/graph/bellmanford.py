import math


# vList = ['A', 'B', 'C', 'D', 'E']
# eList = [('A', 'B', 10), ('A', 'C', 3), ('B', 'C', 1), ('C', 'B', 4), ('B', 'D', 2), ('C', 'D', 8), ('D', 'E', 7), ('E', 'D', 9), ('C', 'E', 2)]

vList = [0,1,2,3]
eList = [(0,1,1), (1,2,-1), (2,3,-1), (3,0,-1)]

def bellmanford(s):
    dist = {i:math.inf for i in vList}
    parent = {i:None for i in vList}
    dist[s] = 0

    def relax(u, v, w):
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parent[v] = u

    for _ in vList:
        for u, v, w in eList:
            relax(u, v, w)
    print(parent)
    print(dist)
    for u, v, w in eList:
        if dist[v] > dist[u] + w:
            return f'negative cycle exist!'

    return dist, parent


def shortest_path(s, e):
    try:
        dist, parent = bellmanford(s)
    except ValueError:
        return 'can\'li find shortest path if the graph has negative cycle!'

    path = [e]
    current = e
    cost = 0

    while parent[current]:
        path.insert(0, parent[current])
        current = parent[current]
    for v in path:
        cost += dist[v]

    if s not in path:
        return f'"{s}" 에서 "{e}"로 가는 경로가 존재하지 않습니다.'

    return f'경로 : {" ".join(path)} \n비용 : {cost}'


# print(shortest_path('A', 'E'))
print(shortest_path(1,3))