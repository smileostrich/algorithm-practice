# prove node
from collections import defaultdict


vertexList = [0,1,2]
edgeList = [(0,1), (1,0), (0,2), (2,0), (1,2), (2,1)]
adjList = defaultdict(int)
# adjList i: [] for i in vertexList



for edge in edgeList:
    adjList[edge[0]] = (edge[1])


print(adjList)
print(adjList[3])
# for k, v in test.items():
#     print(k)
#     print(type(k))
#     print(v)
#     print(type(v))
