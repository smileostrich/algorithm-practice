from collections import deque


N = int(input())
li_matrix = [list(map(int, input().split())) for _ in range(N)]
destination = N*N
for i in range(N):
    for j in range(N):
        if li_matrix[i][j] == 1:
            sx, sy = j, i
            break

mov_knight = [(1,2),(-1,2),(2,1),(-2,1),(1,-2),(-1,-2),(-2,-1),(2,-1)]
mov_bishop = [(1,1),(-1,1),(1,-1),(-1,-1)]
mov_rook = [(0,-1),(-1,0),(1,0),(0,1)]

# dic_horse = {'rook':0,'knight':1,'bishop':2}
dic_horse_rev = {0:'rook', 1:'knight', 2:'bishop'}
visited = [[[[False for _ in range(3)] for _ in range(destination+1)] for _ in range(N)] for _ in range(N)]
visited[sy][sx][1][0] = True
visited[sy][sx][1][1] = True
visited[sy][sx][1][2] = True


def bfs(sx,sy):
    lowest = 9999999
    time = 0
    position = 1
    frontier = deque([(time, position, sx, sy,'rook'),(time, position, sx, sy,'knight'),(time, position, sx, sy,'bishop')])
    while frontier:
        time, position, cur_x, cur_y, horse = frontier.popleft()
        if position == destination:
            if lowest > time:
                lowest = time
        for k in range(3):
            if horse == dic_horse_rev[k]:
                continue
            if not visited[cur_y][cur_x][position][k]:
                visited[cur_y][cur_x][position][k] = True
                frontier.append((time + 1, position, cur_x, cur_y, dic_horse_rev[k]))

        if horse == 'knight':
            for mx,my in mov_knight:
                new_x, new_y = cur_x+mx, cur_y+my
                if 0 <= new_x < N and 0 <= new_y < N:
                    new_position = position
                    if li_matrix[new_y][new_x] == position + 1:
                        new_position = position + 1
                    if not visited[new_y][new_x][new_position][1]:
                        visited[new_y][new_x][new_position][1] = True
                        frontier.append((time+1, new_position, new_x, new_y, 'knight'))

        elif horse == 'bishop':
            for mx,my in mov_bishop:
                new_x, new_y = cur_x+mx, cur_y+my
                if 0 <= new_x < N and 0 <= new_y < N:
                    new_position = position
                    if li_matrix[new_y][new_x] == position + 1:
                        new_position = position + 1
                    if not visited[new_y][new_x][new_position][2]:
                        visited[new_y][new_x][new_position][2] = True
                        frontier.append((time + 1, new_position, new_x, new_y, 'bishop'))

        elif horse == 'rook':
            for mx,my in mov_rook:
                new_x, new_y = cur_x+mx, cur_y+my
                if 0 <= new_x < N and 0 <= new_y < N:
                    new_position = position
                    if li_matrix[new_y][new_x] == position + 1:
                        new_position = position + 1
                    if not visited[new_y][new_x][new_position][0]:
                        visited[new_y][new_x][new_position][0] = True
                        frontier.append((time + 1, new_position, new_x, new_y, 'rook'))
    return lowest
print(bfs(sx,sy))

# from collections import deque
# import math
#
# N = int(input())
# li_matrix = [list(map(int, input().split())) for _ in range(N)]
# destination = N * N
# for i in range(N):
#     for j in range(N):
#         if li_matrix[i][j] == 1:
#             sx, sy = j, i
#             break
#
# mov_knight = [(1, 2), (-1, 2), (2, 1), (-2, 1), (1, -2), (-1, -2), (-2, -1), (2, -1)]
# mov_bishop = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
# mov_rook = [(0, -1), (-1, 0), (1, 0), (0, 1)]
#
# # dic_horse = {'rook':0,'knight':1,'bishop':2}
# visited = [[[[False for _ in range(3)] for _ in range(destination + 1)] for _ in range(N)] for _ in range(N)]
# visited[sy][sx][1][0] = True
# visited[sy][sx][1][1] = True
# visited[sy][sx][1][2] = True
#
#
# def bfs(sx, sy):
#     lowest = math.inf
#     time = 0
#     position = 1
#     frontier = deque(
#         [(time, position, sx, sy, 'rook'), (time, position, sx, sy, 'knight'), (time, position, sx, sy, 'bishop')])
#     while frontier:
#         time, position, cur_x, cur_y, horse = frontier.popleft()
#         if position == destination:
#             if lowest > time:
#                 lowest = time
#         else:
#             for i in range(3):
#
#             if horse == 'knight':
#                 for mx, my in mov_knight:
#                     new_x, new_y = cur_x + mx, cur_y + my
#                     if 0 <= new_x < N and 0 <= new_y < N and not visited[new_y][new_x][position][1]:
#                         visited[new_y][new_x][position][1] = True
#                         if li_matrix[new_y][new_x] == position + 1:
#                             frontier.append((time + 1, position + 1, new_x, new_y, 'knight'))
#                         else:
#                             frontier.append((time + 1, position, new_x, new_y, 'knight'))
#                 if visited[cur_y][cur_x][position][0] == False:
#                     visited[cur_y][cur_x][position][0] = True
#                     frontier.append((time + 1, position, cur_x, cur_y, 'rook'))
#                 if visited[cur_y][cur_x][position][2] == False:
#                     visited[cur_y][cur_x][position][2] = True
#                     frontier.append((time + 1, position, cur_x, cur_y, 'bishop'))
#
#             elif horse == 'bishop':
#                 for mx, my in mov_bishop:
#                     new_x, new_y = cur_x + mx, cur_y + my
#                     if 0 <= new_x < N and 0 <= new_y < N and not visited[new_y][new_x][position][2]:
#                         visited[new_y][new_x][position][2] = True
#                         if li_matrix[new_y][new_x] == position + 1:
#                             frontier.append((time + 1, position + 1, new_x, new_y, 'bishop'))
#                         else:
#                             frontier.append((time + 1, position, new_x, new_y, 'bishop'))
#                 if visited[cur_y][cur_x][position][0] == False:
#                     visited[cur_y][cur_x][position][0] = True
#                     frontier.append((time + 1, position, cur_x, cur_y, 'rook'))
#                 if visited[cur_y][cur_x][position][1] == False:
#                     visited[cur_y][cur_x][position][1] = True
#                     frontier.append((time + 1, position, cur_x, cur_y, 'knight'))
#
#             else:
#                 for mx, my in mov_rook:
#                     new_x, new_y = cur_x + mx, cur_y + my
#                     if 0 <= new_x < N and 0 <= new_y < N and not visited[new_y][new_x][position][0]:
#                         visited[new_y][new_x][position][0] = True
#                         if li_matrix[new_y][new_x] == position + 1:
#                             frontier.append((time + 1, position + 1, new_x, new_y, 'rook'))
#                         else:
#                             frontier.append((time + 1, position, new_x, new_y, 'rook'))
#                 if visited[cur_y][cur_x][position][1] == False:
#                     visited[cur_y][cur_x][position][1] = True
#                     frontier.append((time + 1, position, cur_x, cur_y, 'knight'))
#                 if visited[cur_y][cur_x][position][2] == False:
#                     visited[cur_y][cur_x][position][2] = True
#                     frontier.append((time + 1, position, cur_x, cur_y, 'bishop'))
#     return lowest
#
#
# print(bfs(sx, sy))