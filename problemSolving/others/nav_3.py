import sys


n = 19
edges = 	[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]
adjList = {i:[] for i in range(0,n)}
for v1, v2 in edges:
    adjList[v1].append(v2)
print(adjList)
parent = {}
levelDict = {}
cnt = 0
test = {}


def dfs_visit(s, level):
    for neighbor in adjList[s]:
        if neighbor not in parent:
            parent[neighbor] = s
            test[level] += 1
            dfs_visit(neighbor, level)
def chk(li):
    level = 0
    for neighbor in li:
        level += 1
        test[level] = 0
        dfs_visit(neighbor, level)
    lar = max(test.values())
    result = []
    for k,v in test.items():
        if v != lar:
            result.append((k,v))
    print(result)
    return result


def bfs():
    queue = []
    for k,v in chk(adjList[0]):
        queue.append(k)
    cnt = 0
    while queue:
        test = []
        for current in queue:
            test.extend(chk(adjList[current]))

        queue = []
            # cnt += len(test)
        # queue.extend(test)
    # print(cnt)
bfs()