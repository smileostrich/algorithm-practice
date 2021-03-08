



# dx = [1,1,0,-1,-1,-1,0,1]
# dy = [0,1,1,1,0,-1,-1,-1]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     mat = [[0]*N for _ in range(N)]
#     mid = N//2
#     mat[mid][mid] = 2
#     mat[mid-1][mid-1] = 2
#     mat[mid-1][mid] = 1
#     mat[mid][mid-1] = 1
#     dir = 0
#
#     for _ in range(M):
#         x, y, s = map(int, input().split())
#         x -= 1
#         y -= 1
#         mat[y][x] = s
#         for i in range(8):
#             tmp = []
#             new_x, new_y = x + dx[i], y + dy[i]
#             while 0<=new_y<N and 0<=new_x<N:
#                 if mat[new_y][new_x] == 0:
#                     break
#                 if mat[new_y][new_x] != s:
#                     tmp.append((new_x,new_y))
#                     new_x += dx[i]
#                     new_y += dy[i]
#                 else:
#                     if tmp:
#                         for nx, ny in tmp:
#                             mat[ny][nx] = s
#                     break
#     di_result = {1:0, 2:0, 0:0}
#     for i in mat:
#         for j in i:
#             di_result[j] += 1
#     print(f'#{tc} {di_result[1]} {di_result[2]}')

