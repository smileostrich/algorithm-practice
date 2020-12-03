import math
import heapq

vList = [1,2,3,4,5,6]
eList = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
adjList = {1: [(4, 10), (3, 41), (5, 24), (6, 25)], 2: [(4, 66), (3, 22)], 3: [(5, 24), (1, 41), (2, 22)], 4: [(1, 10), (6, 50), (2, 66)], 5: [(3, 24), (6, 2), (1, 24)], 6: [(5, 2), (4, 50), (1, 25)]}

def dijkstra(adjList, s):
    pqueue = []
    dist = {i:math.inf for i in vList}
    parent = {i:None for i in vList}
    dist[s] = 0

    def relax(u, v, w):
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pqueue, (dist[v], v))
            parent[v] = u

    for v in vList:
        heapq.heappush(pqueue, (dist[v], v))

    while pqueue:
        k, u = heapq.heappop(pqueue)
        if k <= dist[u]:
            for v, w in adjList[u]:
                relax(u, v, w)

    return dist, parent


def shortest_path(s, e):
    dist, parent = dijkstra(adjList, s)
    path = [e]
    current = e
    cost = 0
    # print(parent)
    while parent[current]:
        path.insert(0, parent[current])
        current = parent[current]
    for v in path:
        # print('v',v)
        # print(dist[v])
        # cost += dist[v]
        #여기 체크필요
        cost = dist[v]

    if s not in path:
        return f'"{s}" 에서 "{e}"로 가는 경로가 존재하지 않습니다.'
    # print(path)
    # print(cost)
    return f'path:{path} cost:{cost}'
    # return f'경로 : {" ".join(str(path))} \n비용 : {cost}'
    # 이 부분 숙지

print(shortest_path(5, 2))