# dfs로 구현
# dag판별(사실상 example graph는 dag x)
# dag유무 및 사이클 갯수(단, 사이클이 연결되어 있을 수 있음)
import sys
sys.setrecursionlimit(1000000)

vertexList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
edgeList = [('a', 'b'), ('b', 'e'), ('e', 'd'), ('d', 'b'), ('a', 'd'), ('c', 'f'), ('f', 'f'), ('c', 'e'), ('f', 'g'), ('g', 'e')]



n = int(sys.stdin.readline().rstrip())
# adjList = {i: for i in range(1, n+1)}
adjList = dict(map(lambda x: (x[0]+1,[int(x[1])]), enumerate(sys.stdin.readline().split())))
print(adjList)
parent = {}
levelDict = {}
def dfs_visit(s, level):
    for neighbor in adjList[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            levelDict[neighbor] = level
            dfs_visit(neighbor, level)
        if levelDict[neighbor] == level:
            levelDict[neighbor] = -1
            dfs_visit(neighbor, level)


def dfs():
    level = 0
    for s in range(1,n+1):
        if s not in parent:
            parent[s] = None
            levelDict[s] = level
            dfs_visit(s, level)
            level += 1
    return level


print(dfs())
print(levelDict)
print(parent)