from collections import deque
import math

def bfs():
    dq = deque([(0,0)])
    visited = [[math.inf for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    while dq:
        cx,cy = dq.popleft()
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N:
                val = 0
                if li_matrix[ny][nx] > li_matrix[cy][cx]:
                    val += li_matrix[ny][nx] - li_matrix[cy][cx]
                if visited[ny][nx] > visited[cy][cx] + val + 1:
                    visited[ny][nx] = visited[cy][cx] + val + 1
                    dq.append((nx,ny))
    return visited[-1][-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li_matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bfs()}')


# from collections import deque
# import math
#
# def bfs():
#     dq = deque([(0,0,0)])
#     visited = [[math.inf for _ in range(N)] for _ in range(N)]
#     visited[0][0] = 0
#     low = 1001*N
#     while dq:
#         cx,cy,cnt = dq.popleft()
#         if low > cnt:
#             if cx == N-1 and cy == N-1:
#                 low = cnt
#             else:
#                 for dx,dy in [(0,1),(1,0)]:
#                     nx, ny = cx+dx, cy+dy
#                     cur_weight = li_matrix[cy][cx]
#                     if 0<=nx<N and 0<=ny<N:
#                         val = 0
#                         if li_matrix[ny][nx] > cur_weight:
#                             val += li_matrix[ny][nx] - cur_weight
#                         if visited[ny][nx] > cnt + val + 1:
#                             visited[ny][nx] = cnt + val + 1
#                             dq.append((nx,ny,cnt+val+1))
#     return low
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     li_matrix = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{tc} {bfs()}')