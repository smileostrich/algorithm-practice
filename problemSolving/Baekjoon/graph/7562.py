from collections import deque


def bfs():
    li_visited = [[0 for _ in range(I)] for _ in range(I)]
    li_visited[cy][cx] = 1
    queue = deque([[cx,cy,0]])
    while queue:
        x,y,cnt = queue.popleft()
        if x==tx and y==ty:
            return cnt
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<I and 0<=ny<I and li_visited[ny][nx] == 0:
                queue.append([nx,ny,cnt+1])
                li_visited[ny][nx] = 1

T = int(input())
dir = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
for _ in range(T):
    I = int(input())
    cx,cy = map(int, input().split())
    tx,ty = map(int, input().split())
    print(bfs())