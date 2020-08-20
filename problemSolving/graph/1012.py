import sys


T = int(sys.stdin.readline().rstrip())
M, N, K = map(int, sys.stdin.readline().split())
# position = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
adjList = [[0 for _ in range(M)] for _ in range(N)]
test = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for i in range(K):
    e1, e2 = map(int, sys.stdin.readline().split())
    adjList[e2][e1] = 1
print(adjList)

print(adjList[0][2])
print(adjList[2][0])



def dfs():
    visitedList = []
    stack = [(x, y)]
    while stack:
        current = stack.pop()
        if adjList[M][]
        # if current not in visitedList:
        for i in adjList[current]:
            if i not in visitedList:
                stack.append(i)
        visitedList.append(current)
    print(*visitedList)
    print(len(visitedList))


dfs()


