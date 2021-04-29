dir = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
N, M, K = map(int, input().split())
li_matrix = [[[] for _ in range(N)] for _ in range(N)]
dic_fireball = dict()
for _ in range(M):
    y,x,m,s,d = list(map(int, input().split()))
    li_matrix[y-1][x-1].append([m,s,d])
    if (x-1,y-1) in dic_fireball:
        dic_fireball[(x-1,y-1)] += 1
    else:
        dic_fireball[(x-1,y-1)] = 1

for _ in range(K):
    new_dic = dict()
    for x,y in dic_fireball.keys():
        for m,s,d in li_matrix[y][x]:
            dx,dy = dir[d]
            nx,ny = x,y
            for i in range(s):
                nx,ny = nx+dx, ny+dy
            nx = nx%N
            ny = ny%N
            if (nx, ny) in new_dic:
                new_dic[(nx, ny)] += 1
            else:
                new_dic[(nx, ny)] = 1
            li_matrix[ny][nx].append([m,s,d])
    li_matrix[y][x] = []
    for k,v in new_dic.items():
        if v >= 2:
            x,y = k
            sum_m = 0
            sum_s = 0
            cnt_odd = 0
            cnt_even = 0
            for m,s,d in li_matrix[y][x]:
                sum_m += m
                sum_s += s
                if d%2 == 0:
                    cnt_even += 1
                else:
                    cnt_odd += 1
            li_matrix[y][x] = []
            sum_m = sum_m//5
            if sum_m > 0:
                sum_s = sum_s//v
                if cnt_odd == 0 or cnt_even == 0:
                    li_matrix[y][x] = [[sum_m,sum_s,0],[sum_m,sum_s,2],[sum_m,sum_s,4],[sum_m,sum_s,6]]
                else:
                    li_matrix[y][x] = [[sum_m, sum_s, 1], [sum_m, sum_s, 3], [sum_m, sum_s, 5], [sum_m, sum_s, 7]]
            else:
                li_matrix[y][x] = []
    dic_fireball = new_dic
result = 0
for x,y in dic_fireball.keys():
    for m,s,d in li_matrix[y][x]:
        result += m
print(result)