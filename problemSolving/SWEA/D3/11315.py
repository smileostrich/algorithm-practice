# 정답
# di = [0, 1, 1, 1]
# dj = [1, 1, 0, -1]
# def f(N):
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 o = 0
#                 ni, nj = i, j
#                 while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
#                     o += 1
#                     if o == 5:
#                         return 'YES'
#                     ni += di[k]
#                     nj += dj[k]
#     return 'NO'
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [input() for _ in range(N)]
#     print(f'#{tc} {f(N)}')