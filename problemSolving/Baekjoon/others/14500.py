N, M = map(int, input().split())
li_matrix = [list(map(int, input().split())) for _ in range(N)]
# N, M = 5,5
# li_matrix = [[1, 2, 3, 4, 5,],[5, 4, 3, 2, 1], [2, 3, 4, 5, 6],[6, 5, 4, 3, 2],[1, 2, 1, 2, 1]]
li_type =[([0, 0], [0, 1], [0, 2], [0, 3]),
([0, 0], [1, 0], [2, 0], [3, 0]),
# ㅁ
([0, 0], [0, 1], [1, 1], [1, 0]),
# L
([0, 0], [1, 0], [1, 1], [1, 2]),
([0, 0], [0, 1], [1, 0], [2, 0]),
([0, 0], [0, 1], [0, 2], [1, 2]),
([0, 1], [1, 1], [2, 1], [2, 0]),
([0, 0], [0, 1], [1, 1], [2, 1]),
([1, 0], [1, 1], [1, 2], [0, 2]),
([0, 0], [1, 0], [2, 0], [2, 1]),
([0, 0], [1, 0], [0, 1], [0, 2]),
# 번개
([0, 0], [1, 0], [1, 1], [2, 1]),
([1, 0], [1, 1], [0, 1], [0, 2]),
([2, 0], [1, 0], [1, 1], [0, 1]),
([0, 0], [0, 1], [1, 1], [1, 2]),
# ㅜ
([0, 0], [0, 1], [1, 1], [0, 2]),
([1, 0], [0, 1], [1, 1], [2, 1]),
([1, 0], [1, 1], [1, 2], [0, 1]),
([0, 0], [1, 0], [1, 1], [2, 0])]

def bfs(x,y,type):
    tmp_highest = 0
    global N, M
    for cx,cy in type:
        nx, ny = x+cx, y+cy
        if 0<= nx < M and 0 <= ny < N:
            tmp_highest += li_matrix[ny][nx]
        else:
            return -1
    return tmp_highest

highest = -1
for y in range(N):
    for x in range(M):
        for type in li_type:
            highest = max(highest, bfs(x,y,type))
print(highest)