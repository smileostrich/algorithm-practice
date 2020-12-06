# 40분 (집중 못함)
# pypy로 제출

# from sys import stdin
# import heapq
#
# inp = lambda: stdin.readline().rstrip()
#
#
# def sel_coin(li):
#     global K, cnt_c
#     while True:
#         if K-li[0][1] < 0:
#             heapq.heappop(li)
#             break
#         else:
#             K -= li[0][1]
#             cnt_c += 1
#             break
#
#
# N, K = map(int, inp().split())
# hq_coin = []
# for _ in range(N):
#     tmp_inp = int(inp())
#     heapq.heappush(hq_coin, (-tmp_inp, tmp_inp))
#
# cnt_c = 0
# while True:
#     if K != 0:
#         sel_coin(hq_coin)
#     else:
#         break
# print(cnt_c)



# 리팩토링
from sys import stdin

inp = lambda: stdin.readline().rstrip()


N, K = map(int, inp().split())
li_coin = [int(inp()) for _ in range(N)]
ans = 0

for i in range(N-1, -1, -1):
    ans += K//li_coin[i]
    K %= li_coin[i]
print(ans)
