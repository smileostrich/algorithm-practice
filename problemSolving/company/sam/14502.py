from collections import deque
from itertools import permutations
from copy import deepcopy

dir = [(0,1),(1,0),(-1,0),(0,-1)]

def bfs():
    global high
    li_tmp = deepcopy(li_matrix)
    dq = deque(li_virus)
    cnt = len(li_empty)-3
    while dq:
        x, y = dq.popleft()
        for dx,dy in dir:
            nx, ny = x+dx, y+dy
            if 0<=nx<M and 0<=ny<N and li_tmp[ny][nx] == 0:
                li_tmp[ny][nx] = 2
                cnt -= 1
                dq.append((nx,ny))
    if high < cnt:
        high = cnt


N, M = map(int, input().split())
li_matrix = [list(map(int, input().split())) for _ in range(N)]
li_empty = []
li_virus = []
for y in range(N):
    for x in range(M):
        if li_matrix[y][x] == 0:
            li_empty.append((x,y))
        if li_matrix[y][x] == 2:
            li_virus.append((x,y))
walls = list(permutations(li_empty, 3))
high = 0
for wall in walls:
    for x,y in wall:
        li_matrix[y][x] = 1
    bfs()
    for x,y in wall:
        li_matrix[y][x] = 0
print(high)