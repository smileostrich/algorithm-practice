from collections import deque

N = int(input())
li_matrix = [[0 for _ in range(N)] for _ in range(N)]
cnt_apple = int(input())
for _ in range(cnt_apple):
    y,x = map(int, input().split())
    li_matrix[y-1][x-1] = 1
cnt_smove = int(input())
li_smove = [tuple(input().split()) for _ in range(cnt_smove)]
last_time = li_smove[-1][0]
tail = deque([(0,0)])
dir = [(1,0),(0,1),(-1,0),(0,-1)]
dq = deque([(0,0,0,1,0)])
while dq:
    x,y,face,time,smove = dq.popleft()
    dx,dy = dir[face]
    nx,ny = x+dx, y+dy
    if 0<=nx<N and 0<=ny<N and li_matrix[ny][nx] != 2:
        if not li_matrix[ny][nx] == 1:
            tx, ty = tail.popleft()
            li_matrix[ty][tx] = 0
        li_matrix[ny][nx] = 2
        tail.append((nx, ny))
        n_smove = smove
        n_face = face
        if time == int(li_smove[smove][0]):
            if li_smove[smove][1] == 'D':
                n_face = (n_face+1)%4
            elif li_smove[smove][1] == 'L':
                n_face = (n_face - 1) % 4
            if smove + 1 < cnt_smove:
                n_smove += 1
        dq.append((nx, ny, n_face, time+1, n_smove))
    else:
        print(time)
        break