import math

adjList = dict()
vertexList = []
parent = {}
dic_level = {}

def BFS(s):
    level = {s: 0}
    i = 1
    queue = [s]
    while queue:
        next = []
        for u in queue:
            for neighbor in adjList[u]:
                if neighbor not in level:
                    level[neighbor] = i
                    parent[neighbor] = u
                    next.append(neighbor)
        queue = next
        i += 1
    return len(level.keys())


def connectedSum(graph_nodes, graph_from, graph_to):
    global adjList, vertexList
    vertexList = list(range(1, graph_nodes+1))
    adjList = {i:[] for i in range(1, graph_nodes+1)}
    for a,b in list(zip(graph_from, graph_to)):
        adjList[a].append(b)
        adjList[b].append(a)
    ans = 0
    level = 0
    for s in vertexList:
        if s not in parent:
            parent[s] = None
            dic_level[s] = 0
            ans += math.ceil(BFS(s)**(1/2))
            level += 1
    return ans

print(connectedSum(10,[1,1,2,3,7],[2,3, 4,5,8]))