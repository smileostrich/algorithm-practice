vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for _ in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex

print(dfs(graphs, 0))


# from pythonds.graphs import Graph, Vertex
# from pythonds.basic import Queue
#
#
# def bfs(g,start):
#   start.setDistance(0)
#   start.setPred(None)
#   vertQueue = Queue()
#   vertQueue.enqueue(start)
#   while (vertQueue.size() > 0):
#     currentVert = vertQueue.dequeue()
#     for nbr in currentVert.getConnections():
#       if (nbr.getColor() == 'white'):
#         nbr.setColor('gray')
#         nbr.setDistance(currentVert.getDistance() + 1)
#         nbr.setPred(currentVert)
#         vertQueue.enqueue(nbr)
#     currentVert.setColor('black')