# 3치 40분 200819  2차 30분 1차 fail
# python3   memory : 29380 kb    time : 64 ms
import sys

N = int(sys.stdin.readline().rstrip())
cList = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    cList[i][0] = min(cList[i-1][1] + cList[i][0], cList[i-1][2] + cList[i][0])
    cList[i][1] = min(cList[i-1][0] + cList[i][1], cList[i-1][2] + cList[i][1])
    cList[i][2] = min(cList[i-1][0] + cList[i][2], cList[i-1][1] + cList[i][2])

print(min(cList[N-1]))


# 인터넷 소스 (덧셈 부분 개선 필요)
# import sys
#
# H = int(sys.stdin.readline())
#
# p = [list(map(int, sys.stdin.readline().split())) for i in range(H)]
#
# for i in range(1, len(p)):
#     p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
#     p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
#     p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
# print(min(p[H - 1][0], p[H - 1][1], p[H - 1][2]))