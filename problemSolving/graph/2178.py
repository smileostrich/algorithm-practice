# 2시간 20분
# bfs 구현방법 여러개 써보다가 오래걸림
# 함수 왜 리턴 안됨?? bf에서 return으로 test부르면 none밖에 안옴\
# ==> return 값을 함수 호출에도 넣어줘야됨(너무 당연한건데 실수)(사소한 실수 줄이기...ㅠㅠ 이거때문에 1시간 넘게 씀)
# 보통 런타임 에러는 재귀 에러가 제일 많음.
import sys
sys.setrecursionlimit(100000)


def bfs(x, y):
    level = {(x,y):0}
    parent = {(x,y):None}
    queue = [(x,y)]
    i = 1
    dis = 1
    while queue:
        next = []
        for x, y in queue:
            dis += 1
            mat[y][x] = 0
            for dx, dy in near:
                newX, newY = dx + x, dy + y
                if (newX, newY) not in level:
                    if (0 <= newX < M) and (0 <= newY < N) and (mat[newY][newX]) == 1:
                        next.append((newX, newY))
                        level[(newX, newY)] = i
                        parent[(newX, newY)] = (x, y)
        i += 1
        queue = next
    return test(parent, M - 1, N - 1, 0)


def test(parent, x, y, c):
    tmp = parent[(x, y)]
    c += 1
    if tmp != None:
        return test(parent, *tmp, c)
    else:
        return c


N, M = map(int, sys.stdin.readline().split())
mat = [[0]*(M) for _ in range(N)]
near = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(N):
    for idxj, j in enumerate(sys.stdin.readline().rstrip()):
        j = int(j)
        if j == 1:
            mat[i][idxj] = 1
print(bfs(0,0))








# import sys
# sys.setrecursionlimit(100000)
#
#
# def bfs(x, y):
#     level = {(x,y):0}
#     parent = {(x,y):None}
#     queue = [(x,y)]
#     i = 1
#     dis = 1
#     while queue:
#         next = []
#         for x, y in queue:
#             dis += 1
#             mat[y][x] = 0
#             for dx, dy in near:
#                 newX, newY = dx + x, dy + y
#                 if (newX, newY) not in level:
#                     if (0 <= newX < M) and (0 <= newY < N) and (mat[newY][newX]) == 1:
#                         next.append((newX, newY))
#                         level[(newX, newY)] = i
#                         parent[(newX, newY)] = (x, y)
#         i += 1
#         queue = next
#     test(parent, M - 1, N - 1, 0)
#     return -1
#
#
# def test(parent, x, y, c):
#     tmp = parent[(x, y)]
#     c += 1
#     if tmp != None:
#         test(parent, *tmp, c)
#     else:
#         print(c)
#         return -1
#
#
# N, M = map(int, sys.stdin.readline().split())
# mat = [[0]*(M) for _ in range(N)]
# near = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# for i in range(N):
#     for idxj, j in enumerate(sys.stdin.readline().rstrip()):
#         j = int(j)
#         if j == 1:
#             mat[i][idxj] = 1
# bfs(0,0)
