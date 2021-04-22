import heapq, math

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
    while parent[current]:
        path.insert(0, parent[current])
        current = parent[current]
    for v in path:
        cost = dist[v]
    return cost


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjList = {i:[] for i in range(0,N+1)}
    vList = [i for i in range(0,N+1)]
    for _ in range(E):
        s,e,w = map(int, input().split())
        adjList[s].append((e,w))
    print(f'#{tc} {shortest_path(0,N)}')
