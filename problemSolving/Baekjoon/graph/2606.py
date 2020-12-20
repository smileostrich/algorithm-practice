# dfs로 품 33분 (양방향에서 조금 헷갈림, 기타 런타임에러= 코딩실수 등에서 많이 잡아먹음)
import sys


def dfs(vertexN, edgeN):
    if vertexN < 2:
        print(0)
    adjacencyList = [[] for _ in range(vertexN + 1)]
    stack = [1]
    visitedList = []

    for _ in range(edgeN):
        e1, e2 = map(int, sys.stdin.readline().split())
        adjacencyList[e1].append(e2)
        adjacencyList[e2].append(e1)
    # print(adjacencyList)
    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if neighbor not in stack:
                if neighbor not in visitedList:
                    stack.append(neighbor)
        visitedList.append(current)

    print(len(visitedList)-1)

vertexN = int(sys.stdin.readline().rstrip())
edgeN = int(sys.stdin.readline().rstrip())
dfs(vertexN, edgeN)