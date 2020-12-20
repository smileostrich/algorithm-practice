# 54분
import sys


near = [(1,0), (0,1), (0,-1), (-1,0)]

def bfs(cx, cy, tcnt):
    queue = [(cx, cy)]
    while queue:
        x, y = queue.pop(0)
        for di, dj in near:
            newX, newY = x+di, y+dj
            if 0 <= newX < N and 0 <= newY < N and li[newX][newY] == 1:
                queue.append((newX, newY))
                li[newX][newY] = 0
                tcnt += 1
    return tcnt


cnt = 0
tli = []
N = int(sys.stdin.readline().rstrip())
# 이게 내소스 밑에 부분은 인터넷 참조(순간 생각 안남ㅠㅠ)
# li = [[0]*N for _ in range(N)]
# for i in range(N):
#     test = sys.stdin.readline().rstrip()
#     for idx, j in enumerate(test):
#         if int(j) == 1:
#             li[i][idx] = 1
li = []
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().rstrip())))

for idxi, i in enumerate(li):
    for idxj, j in enumerate(i):
        if j == 1:
            li[idxi][idxj] = 0
            tli.append(bfs(idxi, idxj, 1))
            cnt += 1

print(cnt)
tli.sort()
for i in tli:
    print(i)