# 2차시도 성공 33분
import sys

N = int(sys.stdin.readline())
t = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
li = [0] * N

for idx, i in enumerate(t):
    if idx != 0:
        r,g,b = map(int, i)
        t[idx][0], t[idx][1], t[idx][2] = min(t[idx][0] + t[idx-1][1], t[idx][0] + t[idx-1][2]), min(t[idx][1] + t[idx-1][0], t[idx][1] + t[idx-1][2]), min(t[idx][2] + t[idx-1][0], t[idx][2] + t[idx-1][1])
        li[idx] = min(t[idx][0], t[idx][1], t[idx][2])
print(li[N-1])



#내가 안품 1시간 지나서 인터넷 보고 적은거임

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
