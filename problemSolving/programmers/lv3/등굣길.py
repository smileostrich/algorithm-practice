from collections import deque

def bfs(m,n, puddles):
    li_matrix = [[100000000 for _ in range(m)] for _ in range(n)]
    li_t2 = [[0 for _ in range(m)] for _ in range(n)]
    li_matrix[0][1] = 1
    li_matrix[1][0] = 1
    dq = deque([(0,1,1),(1,0,1)])
    while dq:
        x,y,cnt = dq.popleft()
        for dx,dy in [(0,1),(1,0)]:
            nx,ny = x+dx, y+dy
            if 0<= nx<m and 0<=ny<n and [nx,ny] not in puddles and li_matrix[ny][nx] >= cnt+1:
                dq.append((nx,ny,cnt+1))
                li_matrix[ny][nx] = cnt+1
                li_t2[ny][nx] += 1
    return li_t2[-1][-1] % 1000000007



def solution(m, n, puddles):
    for i in range(len(puddles)):
        tx,ty = puddles[i]
        puddles[i] = [tx-1, ty-1]
    return bfs(m,n, puddles)

print(solution(4, 3, [[2, 2]]))