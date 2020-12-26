from collections import deque
import heapq

n = 19
edgeList = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]
# n = 14
# edgeList = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]
adjList = {v:[] for v in range(n)}
for edge in edgeList:
    adjList[edge[0]].append(edge[1])
print(adjList)

def dfs(s):
    stack = [s]
    visited = {}

    while stack:
        current = stack.pop()
        for neighbor in adjList[current]:
            if neighbor not in visited:
                visited[neighbor] = True
                stack.append(neighbor)
    return (-len(visited), (s, len(visited)))


def test(s):
    queue = deque([s])
    cnt = 0
    while queue:
        current = queue
        queue = []
        # current = queue.popleft()
        tmp = []
        heapq.heapify(tmp)
        for i in adjList[current]:
            heapq.heappush(tmp, dfs(i))
        print(tmp)
        print(len(tmp)-1)
        cnt += len(tmp)-1
        if tmp:
            heapq.heappop(tmp)
            for j in tmp:
                queue.append(j[1][0])
    print(cnt)
test(0)