# 1시간 30분
import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    li = [0]* (N+1)

    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        li[a] = b
    li.insert
    result = 1
    tmp = li[1]
    for i in range(2, len(li)):
        if tmp > li[i]:
            tmp = li[i]
            result += 1

    print(result)


# import sys
#
# T = int(sys.stdin.readline().rstrip())
# result = []
# for _ in range(T):
#     N = int(sys.stdin.readline().rstrip())
#     li = [[] for _ in range(N+1)]
#
#     for i in range(N):
#         a, b = map(int, sys.stdin.readline().split())
#         li[a] = [a,b]
#
#     def ncheck(idx):
#         tmp = li[idx][1]
#         if len(li) > 2:
#             for i in range(idx+1, len(li)):
#                 if tmp < li[i][1]:
#                     li.pop(i)
#                     ncheck(idx)
#                     break
#
#     for i in range(1, len(li)):
#         if len(li)-1 <= i:
#             break
#         ncheck(i)
#
#     result.append(len(li)-1)
# for i in result:
#     print(i)