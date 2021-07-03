
def queensAttack(n, k, r_q, c_q, obstacles):
    dir = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    s = set()
    for y,x in obstacles:
        s.add((y,x))
    ans = 0
    for nx,ny in dir:
        cur_y, cur_x = r_q, c_q
        while 0 < cur_y <= n and 0 < cur_x <= n:
            if (cur_y, cur_x) not in s:
                ans += 1
            else:
                break
            cur_x,cur_y = cur_x+nx, cur_y+ny
        ans -= 1
    return ans

    # li_matrix = [[0 for _ in range(n)] for _ in range(n)]
    # r_q, c_q = r_q-1, c_q-1
    # li_matrix[r_q][c_q] = 1
    # for y, x in obstacles:
    #     li_matrix[y-1][x-1] = -1
    # cnt = 0
    # for d_x,d_y in dir:
    #     nx, ny = c_q, r_q
    #     while True:
    #         nx, ny = nx + d_x, ny + d_y
    #         if 0<=nx<n and 0<=ny<n and li_matrix[ny][nx] != -1:
    #             li_matrix[ny][nx] = 2
    #             cnt += 1
    #         else:
    #             break
    # return cnt





print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))