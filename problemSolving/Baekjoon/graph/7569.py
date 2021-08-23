from collections import deque


M, N, H = map(int, input().split())
li_matrix = [[] for _ in range(H)]
dir = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
queue = deque([])
for i in range(H):
    for j in range(N):
        li_t = list(map(int, input().split()))
        li_matrix[i].append(li_t)
        for di, dv in enumerate(li_t):
            if dv == 1:
                queue.append([i,di,j,1])
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if li_matrix[i][j][k] == 1:
#                 queue.append([i,k,j,1])
midx = 0
while queue:
    h,x,y,idx = queue.popleft()
    if idx > midx:
        midx = idx
    for th,tx,ty in dir:
        nh,nx,ny = h+th,x+tx,y+ty
        if 0<= nh <H and 0<=nx<M and 0<=ny<N and li_matrix[nh][ny][nx]==0:
            queue.append([nh, nx, ny,idx+1])
            li_matrix[nh][ny][nx] = idx + 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if li_matrix[i][j][k] == 0:
                print(-1)
                exit(0)
print(midx-1)