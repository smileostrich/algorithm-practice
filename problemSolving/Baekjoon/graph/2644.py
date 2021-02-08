import sys
from collections import deque
inp = lambda: sys.stdin.readline().rstrip()

total_p = int(inp())
p1, p2 = map(int, inp().split())
dic_rel = {i:[] for i in range(1, total_p+1)}

for i in range(int(inp())):
    t1, t2 = map(int, inp().split())
    dic_rel[t1].append(t2)

def bfs(s):
    visited = []
    q = deque([s])

    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            q.extend(dic_rel[n])
    return visited
print(bfs(7))
# {1: [2, 3], 2: [7, 8, 9], 3: [], 4: [5, 6], 5: [], 6: [], 7: [], 8: [], 9: []}
