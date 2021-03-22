def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret


def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret

T = int(input())
# T = 1
for tc in range(1, T+1):
    N, dir = input().split()
    N = int(N)
    # N, dir = 5, 'up'
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # matrix = [[4, 8, 2, 4, 0],[4, 4, 2, 0, 8],[8, 0, 2, 4, 4],[2, 2, 2, 2, 8],[0, 2, 2, 0, 0]]
    if dir == 'up':
        matrix = rotate_270(matrix)
    elif dir == 'right':
        matrix = rotate_180(matrix)
    elif dir == 'down':
        matrix = rotate_90(matrix)
    for i in range(N):
        for j in range(N):
            for k in range(j+1, N):
                if matrix[i][k] == matrix[i][j]:
                    matrix[i][j] *= 2
                    matrix[i][k] = 0
                    break
                elif matrix[i][k] == 0:
                    continue
                else:
                    break
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                for k in range(j + 1, N):
                    if matrix[i][k] != 0:
                        matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                        break
    if dir == 'up':
        matrix = rotate_90(matrix)
    elif dir == 'right':
        matrix = rotate_180(matrix)
    elif dir == 'down':
        matrix = rotate_270(matrix)
    print(f'#{tc}')
    for i in matrix:
        print(*i)

# # 추억의 2048게임
# # import sys
# #
# # sys.stdin = open("input.txt", "r")
# T = int(input())
# for li in range(1, T+1):
#     N, direct = input().split()
#     N = int(N)
#     board = [list(map(int, input().split())) for _ in range(N)]
#     # 먼저 합치고, 빈칸 채우기
#     if direct == "up":
#         # 세로 끼리 합치기
#         for i in range(N):
#             for j in range(N-1):
#                 for k in range(j+1, N):
#                     if board[k][i] != 0:
#                         if board[j][i] == board[k][i]:
#                             board[j][i] = board[j][i] * 2
#                             board[k][i] = 0
#                         break
#         # 빈칸 채워넣기 앞에서부터 검색해서 빈칸이면 가장 앞에 있는 숫자 가져와서 채워넣기
#         for i in range(N):
#             for j in range(N-1):
#                 if board[j][i] == 0:
#                     for k in range(j+1, N):
#                         if board[k][i] != 0:
#                             board[j][i] = board[k][i]
#                             board[k][i] = 0
#                             break
#     elif direct == "right":
#         # 오른쪽으로 밀기
#         for i in range(N):
#             for j in range(N - 1, 0, -1):
#                 for k in range(j-1, -1, -1):
#                     if board[i][k] != 0:
#                         if board[i][j] == board[i][k]:
#                             board[i][j] = board[i][j] * 2
#                             board[i][k] = 0
#                         break
#         # 빈칸 채워넣기 앞에서부터 검색해서 빈칸이면 가장 앞에 있는 숫자 가져와서 채워넣기
#         for i in range(N):
#             for j in range(N - 1, 0, -1):
#                 if board[i][j] == 0:
#                     for k in range(j - 1, -1, -1):
#                         if board[i][k] != 0:
#                             board[i][j] = board[i][k]
#                             board[i][k] = 0
#                             break
#
#     elif direct == "down":
#         # 세로 끼리 합치기
#         for i in range(N):
#             for j in range(N - 1, 0, -1):
#                 for k in range(j - 1, -1, -1):
#                     if board[k][i] != 0:
#                         if board[j][i] == board[k][i]:
#                             board[j][i] = board[j][i] * 2
#                             board[k][i] = 0
#                         break
#         # 빈칸 채워넣기 앞에서부터 검색해서 빈칸이면 가장 앞에 있는 숫자 가져와서 채워넣기
#         for i in range(N):
#             for j in range(N - 1, 0, -1):
#                 if board[j][i] == 0:
#                     for k in range(j - 1, -1, -1):
#                         if board[k][i] != 0:
#                             board[j][i] = board[k][i]
#                             board[k][i] = 0
#                             break
#     elif direct == "left":
#         # 왼쪽으로 밀기
#         for i in range(N):
#             for j in range(N - 1):
#                 for k in range(j + 1, N):
#                     if board[i][k] != 0:
#                         if board[i][j] == board[i][k]:
#                             board[i][j] = board[i][j] * 2
#                             board[i][k] = 0
#                         break
#         # 빈칸 채워넣기 앞에서부터 검색해서 빈칸이면 가장 앞에 있는 숫자 가져와서 채워넣기
#         for i in range(N):
#             for j in range(N - 1):
#                 if board[i][j] == 0:
#                     for k in range(j + 1, N):
#                         if board[i][k] != 0:
#                             board[i][j] = board[i][k]
#                             board[i][k] = 0
#                             break
#     print("#%d" % li )
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j], end=" ")
#         print()