T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    core = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j]:
                core.append((i, j))
    min_wire = n*n
    max_core = 0
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [(0, 0, 0, arr)]
    while stack:
        idx, n_core, wire, arr = stack.pop()
        if idx == len(core):
            if n_core > max_core or (n_core == max_core and wire < min_wire):
                max_core, min_wire = n_core, wire
        elif n - idx + n_core > max_core or (n - idx + n_core == max_core and wire <= min_wire):
            stack.append((idx + 1, n_core, wire, [lst[:] for lst in arr]))
            for d in range(4):
                x, y = core[idx]
                dx, dy = delta[d]
                x, y = x + dx, y + dy
                wire2 = wire
                arr2 = [l[:] for l in arr]
                while 0 <= x < n and 0 <= y < n and arr[x][y] == 0:
                    arr2[x][y] = 1
                    wire2 += 1
                    x += dx
                    y += dy
                if x == -1 or x == n or y == -1 or y == n:
                    stack.append((idx + 1, n_core + 1, wire2, arr2))
    print('#{} {}'.format(tc, min_wire))

# import copy
#
# def bfs(s):
#     t_matrix = copy.deepcopy(li_matrix)
#     level = {s:0}
#     i = 1
#     frontier = [s]
#     while frontier:
#         next = []
#         for x,y in frontier:
#             smallest = 99999
#             cur_d = -1
#             for d in range(4):
#                 nx = x
#                 ny = y
#                 cnt = 0
#                 while True:
#                     nx, ny = dx[d] + nx, dy[d] + ny
#                     if 0<=nx<N and 0<=ny<N:
#                         cnt += 1
#                         if li_matrix[ny][nx] != 0:
#                             break
#                     else:
#                         ne
#                         if cnt < smallest:
#                             cur_d = d
#                         break
#             nx = x
#             ny = y
#             for _ in smallest:
#                 nx, ny = dx[cur_d] + nx, dy[cur_d] + ny
#                 t_matrix[ny][nx] = 2
#
#
#
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     li_matrix = [list(map(int, input().split())) for _ in range(N)]
#     li_core = []
#     for i in range(1, N-1):
#         for j in range(1, N-1):
#             if li_matrix[i][j] == 1:
#                 li_core.append((j,i))
#     for i in li_core:
#
#
#     print(li_core)
#     print(f'#{tc} ')
