import sys
from copy import deepcopy
import math
sys.setrecursionlimit(100000)

def dfs(li_cur, idx, cnt):
    global low
    if idx == len(li_cctv):
        t_cnt = 0
        for cur in li_cur:
            t_cnt += cur.count(0)
        low = min(low, t_cnt)
        return
    else:
        li_rec = deepcopy(li_cur)
        x,y,cctv = li_cctv[idx]
        for li_inner in dic_cctv[cctv]:
            for dx, dy in li_inner:
                nx, ny = x, y
                while True:
                    nx, ny = nx + dx, ny + dy
                    if 0 <= nx < M and 0 <= ny < N and li_rec[ny][nx] != 6:
                        if li_rec[ny][nx] == 0:
                            li_rec[ny][nx] = -1
                            cnt += 1
                    else:
                        break
            dfs(li_rec, idx+1, cnt)
            li_rec = deepcopy(li_cur)


N, M = map(int, input().split())
li_matrix = [list(map(int, input().split())) for _ in range(N)]
dic_cctv = {1:[[(0,1)],[(1,0)],[(-1,0)],[(0,-1)]], 2: [[(0,1),(0,-1)],[(1,0),(-1,0)]], 3:[[(0,-1),(1,0)],[(1,0),(0,1)],[(0,1),(-1,0)],[(-1,0),(0,-1)]],
            4:[[(-1,0),(0,-1),(1,0)],[(0,-1),(1,0),(0,1)],[(1,0),(0,1),(-1,0)],[(0,1),(-1,0),(0,-1)]], 5:[[(0,1),(1,0),(-1,0),(0,-1)]]}

li_wall = []
li_cctv = []
cnt_empty = 0
for y in range(N):
    for x in range(M):
        tmp = li_matrix[y][x]
        if tmp == 0:
            cnt_empty += 1
        elif tmp == 1:
            li_cctv.append((x, y, 1))
        elif tmp == 2:
            li_cctv.append((x, y, 2))
        elif tmp == 3:
            li_cctv.append((x, y, 3))
        elif tmp == 4:
            li_cctv.append((x, y, 4))
        elif tmp == 5:
            li_cctv.append((x, y, 5))
        elif tmp == 6:
            li_wall.append((x, y, 6))
low = math.inf
dfs(li_matrix,0,0)
print(low)
# print(cnt_empty, highest)