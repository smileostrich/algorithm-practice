# re
from collections import deque
import math

def solution(board):
    n = len(board)
    visited = [[math.inf for _ in range(n)] for _ in range(n)]
    ds = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    q = deque()
    q.append((0, 0, 0, -1))
    visited[0][0] = 0
    while q:
        y, x, c, t = q.popleft()
        for i in range(4):
            ay, ax = y + ds[i][0], x + ds[i][1]

            if 0 <= ay < n and 0 <= ax < n and not board[ay][ax]:
                cost = 100 if t == i or t == -1 else 600
                new_cost = c + cost

                if visited[ay][ax] >= new_cost:
                    visited[ay][ax] = new_cost
                    q.append((ay, ax, new_cost, i))

    answer = visited[n - 1][n - 1]
    return answer

print(solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))



# from collections import deque
#
# def solution(board):
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     N = len(board)
#     visited = [[-1] * N for _ in range(N)]
#     Q = deque()
#     Q.append([0, 0, 0, 0])
#     Q.append([0, 0, 0, 1])
#     visited[0][0] = 0
#     while Q:
#         now_cost, i, j, d = Q.popleft()
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#
#             # 경계체크
#             if ni < 0 or nj < 0 or ni >= N or nj >= N:
#                 continue
#             # 벽체크
#             if board[ni][nj] == 1:
#                 continue
#             # 뒤로가기 체크
#             if abs(k-d) == 2:
#                 continue
#             cost = 100 if k == d else 600
#             new_cost = now_cost + cost
#             if visited[ni][nj] == -1 or new_cost <= visited[ni][nj]:
#                 visited[ni][nj] = new_cost
#                 Q.append([new_cost, ni, nj, k])
#
#     return visited[N-1][N-1]