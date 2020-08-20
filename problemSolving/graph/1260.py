import sys

N, M, V = map(int, sys.stdin.readline().split())
adjacencyList = [[] for _ in range(N+1)]

for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    adjacencyList[v1].append(v2)
    adjacencyList[v2].append(v1)

def dfs():
    # for i in adjacencyList:
    #     i.sort(reverse=True)
    visitedList = []
    stack = [V]
    while stack:
        current = stack.pop()
        adjacencyList[current].sort(reverse=True)
        if current not in visitedList:
            visitedList.append(current)
            for i in adjacencyList[current]:
                if i not in visitedList:
                    stack.append(i)
    print(*visitedList)

def bfs():
    # for i in adjacencyList:
    #     i.sort()
    visitedList = []
    queue = [V]
    while queue:
        current = queue.pop(0)
        adjacencyList[current].sort()
        if current not in visitedList:
            visitedList.append(current)
            for i in adjacencyList[current]:
                if i not in visitedList:
                    queue.append(i)
    print(*visitedList)

dfs()
bfs()
