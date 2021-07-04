N = int(input())
li_candies = []
for _ in range(N):
    li_candies.append(list(input()))
dir = [(1,0),(0,1)]
largest = 0
for y in range(N):
    for x in range(N):
        val = li_candies[y][x]
        cnt = 0
        for t_x, t_y in [(0, 1), (0, -1)]:
            f_x, f_y = x + t_x, y + t_y
            while True:
                if 0 <= f_x < N and 0 <= f_y < N and li_candies[f_y][f_x] == val:
                    cnt += 1
                    f_x, f_y = f_x + t_x, f_y + t_y
                else:
                    break
        cnt += 1
        if cnt > largest:
            largest = cnt
        cnt = 0
        for t_x, t_y in [(1, 0),(-1, 0)]:
            f_x, f_y = x + t_x, y + t_y
            while True:
                if 0 <= f_x < N and 0 <= f_y < N and li_candies[f_y][f_x] == val:
                    cnt += 1
                    f_x, f_y = f_x + t_x, f_y + t_y
                else:
                    break
        cnt += 1
        if cnt > largest:
            largest = cnt

for y in range(N):
    for x in range(N):
        for d_x, d_y in dir:
            n_x, n_y = x+d_x, y+d_y
            if 0<=n_y<N and 0<=n_x<N:
                li_candies[n_y][n_x], li_candies[y][x] = li_candies[y][x], li_candies[n_y][n_x]
                for c_x, c_y in [(n_x,n_y),(x,y)]:
                    cnt = 0
                    val = li_candies[c_y][c_x]
                    for t_x, t_y in [(0,1),(0,-1)]:
                        f_x, f_y = c_x + t_x, c_y + t_y
                        while True:
                            if 0<=f_x<N and 0<=f_y<N and li_candies[f_y][f_x] == val:
                                cnt += 1
                                f_x, f_y = f_x + t_x, f_y + t_y
                            else:
                                break
                    cnt += 1
                    if cnt > largest:
                        largest = cnt
                    cnt = 0
                    for t_x, t_y in [(1,0),(-1,0)]:
                        f_x, f_y = c_x + t_x, c_y + t_y
                        while True:
                            if 0<=f_x<N and 0<=f_y<N and li_candies[f_y][f_x] == val:
                                cnt += 1
                                f_x, f_y = f_x + t_x, f_y + t_y
                            else:
                                break
                    cnt += 1
                    if cnt > largest:
                        largest = cnt
                li_candies[n_y][n_x], li_candies[y][x] = li_candies[y][x], li_candies[n_y][n_x]
print(largest)