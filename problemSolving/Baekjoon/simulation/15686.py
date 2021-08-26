from itertools import combinations
N, M = map(int, input().split())
li_matrix = [list(map(int, input().split())) for _ in range(N)]
li_chicken = []
li_home = []
for i in range(N):
    for j in range(N):
        if li_matrix[i][j] == 2:
            li_chicken.append((j,i))
        elif li_matrix[i][j] == 1:
            li_home.append((j,i))

def distance(x,y,stores):
    t_lo = 100000000
    for s_x,s_y in stores:
        if abs(s_x-x)+abs(s_y-y) < t_lo:
            t_lo = abs(s_x-x)+abs(s_y-y)
    return t_lo

lowest = 100000000
for stores in combinations(li_chicken,M):
    cur_distance = 0
    for h_x,h_y in li_home:
        cur_distance += distance(h_x,h_y,stores)
        if lowest < cur_distance:
            break
    else:
        if cur_distance < lowest:
            lowest = cur_distance
print(lowest)