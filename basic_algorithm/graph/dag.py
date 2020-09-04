# dfs로 구현
# dag판별(사실상 example graph는 dag x)
# dag유무 및 사이클 갯수(단, 사이클이 연결되어 있을 수 있음)

vertexList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
edgeList = [('a', 'b'), ('b', 'e'), ('e', 'd'), ('d', 'b'), ('a', 'd'), ('c', 'f'), ('f', 'f'), ('c', 'e'), ('f', 'g'), ('g', 'e')]

adjList = {i:[] for i in vertexList}
for v1, v2 in edgeList:
    adjList[v1].append(v2)

parent = {}
tmpList = []
firstcycle = []
cycleList = []
print(adjList)

# 미구현
# 어차피 dfs니까 연결되어있는 사이클이면 리스트1에 확인 후 추가, 비연결 사이클이면 새로 또 추가
def dfs_visit(adjList, s):
    for neighbor in adjList[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            dfs_visit(adjList, neighbor)
        elif neighbor == s:
            continue
        elif firstcycle:
            tmpList.append(tmpList[-1] + [s])
        else:
            # dfs에서 s가 두번 이상 들어왔을때, 해당 vertex와 이전 사이클이 연결되어있을 경우.
            if cycleList and (neighbor in cycleList[-1]):
                tmpList.append(cycleList[-1] + [s])
                firstcycle.append(cycleList[-1] + [s])
            # 새로운 cycle
            else:
                firstcycle.append(neighbor)
                count_cycle(s)
                tmpList.append(firstcycle.copy())


# cycle 갯수(떨어져 있는것만)
def count_cycle(s):
    firstcycle.append(s)
    if parent[s] not in firstcycle:
        count_cycle(parent[s])


def dfs(vList, adjList):
    for s in vList:
        if s not in parent:
            parent[s] = None
            tmpList.clear()
            firstcycle.clear()
            dfs_visit(adjList, s)
            print(tmpList)

            for i in tmpList:
                cycleList.append(i)


dfs(vertexList, adjList)
print(parent)
print(cycleList)