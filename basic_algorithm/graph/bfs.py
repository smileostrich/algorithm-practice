vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)


def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for _ in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while queue:
        current = queue.pop(0)
        for neighbor in adjacencyList[current]:
            if neighbor not in visitedList:
                queue.append(neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs, 0))
