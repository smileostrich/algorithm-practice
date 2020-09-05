# 사소한 실수로 10분 지체
# dfs 알고리즘 바꿔서 10분 지체
# 38분 1차. 디버깅시작
# dfs


# elif neighbor in result:
# result.append(s)
# elif neighbor == parent[neighbor]:
# parent[s] = neighbor
# result.append(s)
# elif neighbor not in cycleList:
# current = s
# cycleList.append(current)
# for _ in range(time):
#     current = parent[current]
#     cycleList.append(current)
import sys


def dfs_v(s):
    for neighbor in adjList[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            dfs_v(neighbor)
        elif neighbor == s:
            parent[neighbor] = s
            cycleList.append(neighbor)
        elif (neighbor in result) or neighbor in cycleList:
            parent[s] = neighbor
            result.append(s)
        else:
            parent[neighbor] = s
            cycleList.append(s)
            future = parent[s]
            while future != s:
                cycleList.append(future)
                future = parent[future]



def dfs():
    for s in range(1, A+1):
        if s not in parent:
            parent[s] = None
            dfs_v(s)
    print(result)
    print(len(result))
    print(cycleList)


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    A = int(sys.stdin.readline().rstrip())
    eList = list(map(int, sys.stdin.readline().split()))
    adjList = {i+1:[] for i in range(A)}
    parent = {}
    cycleList = []
    result = []
    for idx, i in enumerate(eList):
        adjList[idx+1].append(i)
    dfs()
