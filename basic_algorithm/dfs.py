# vertexList = ['0', '1', '2', '3', '4', '5', '6']
# edgeList = [(0,1), (0,2), (1,0), (1,3), (2,0), (2,4), (2,5), (3,1), (4,2), (4,6), (5,2), (6,4)]
# graphs = (vertexList, edgeList)
#
# # def dfs(vertexList, edgeList, start):
# def dfs(start):
#     # vertexList, edgeList = vertexList, edgeList
#     visited = []
#     stack = [start]
#     adjacencyList = [[] for _ in vertexList]
#
#     for i in edgeList:
#         adjacencyList[i[0]].append(i[1])
#
#     while stack:
#         current = stack.pop()
#         for neighbor in adjacencyList[current]:
#             if not neighbor in visited:
#                 stack.append(neighbor)
#         visited.append(cugdrvxffasds-rrent)
#     return visited
#
# print(dfs(0))


from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')