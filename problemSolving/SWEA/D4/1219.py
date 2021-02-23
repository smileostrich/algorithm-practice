from collections import deque
def bfs(s):
    visited = [0]*100
    deq = deque([s])
    while deq:
        cur = deq.popleft()
        for neighbor in adjdict[cur]:
            if not visited[neighbor]:
                deq.append(neighbor)
        visited[cur] = 1
    return visited
for _ in range(1, 11):
    tc, pair = map(int, input().split())
    adjdict = {i:[] for i in range(100)}
    li_tmp = list(map(int, input().split()))
    for i in range(0,len(li_tmp),2):
        adjdict[li_tmp[i]].append(li_tmp[i+1])
    print(f'#{tc} {bfs(0)[-1]}')