from collections import deque
N, M = map(int, input().split())

li_matrix = [list(map(int, input().split())) for _ in range(N)]
li_op = list(map(int, input().split()))

dir = [(1,0),(0,1),(-1,0),(0,-1)]

size_x, size_y = li_op[1], li_op[0]
d_x, d_y = li_op[5]-1, li_op[4]-1
s_x,s_y = li_op[3]-1, li_op[2]-1

dq = deque([(0, s_x, s_y)])
visited = [[False for _ in range(M)] for _ in range(N)]

def check(x, y):
    for i in range(size_y):
        for j in range(size_x):
            new_x, new_y = x + j, y + i
            if 0 <= new_x < M and 0 <= new_y < N and li_matrix[new_y][new_x] == 0:
                continue
            else:
                return False
    return True


while dq:
    time, c_x, c_y = dq.popleft()
    if c_x == d_x and c_y == d_y:
        result = time
        break
    for mx, my in dir:
        new_x, new_y = c_x+mx, c_y+my
        if 0 <= new_x < M and 0 <= new_y < N and li_matrix[new_y][new_x] == 0 and not visited[new_y][new_x]:
            if check(new_x, new_y):
                dq.append((time+1, new_x, new_y))


print(result)