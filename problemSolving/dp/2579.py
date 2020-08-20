# fail
# import sys
#
# N = int(sys.stdin.readline().rstrip())
# pList = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
#
# if N == 1:
#     print(pList[0])
# elif N == 2:
#     print(sum(pList))
# elif N == 3:
#     print(max(pList[0]+pList[2], pList[1]+pList[2]))
# else:
#     result = [0] * N
#     result[0] = pList[0]
#     result[1] = pList[0] + pList[1]
#     result[2] = max(pList[0]+pList[2], pList[1]+pList[2])
#     for i in range(3, N):
#         result[i] = max(pList[i]+result[i-2], pList[i]+pList[i-1]+result[i-3])
#     print(result[-1])


# 인터넷 소스
# from sys import stdin
#
# a,b,c = 0,0,0
#
# n = int(stdin.readline())
# for _ in range(n):
#     pb = int(stdin.readline())
#     d_0,d_1,d_2 = max(b,c),a+pb,b+pb
#     a,b,c = d_0,d_1,d_2
#
# print(max(d_2,d_1))

# 인터넷 소스2
# import sys
# read = lambda: sys.stdin.readline().rstrip()
# s1, s2 = 0, 0
# a,b,c,d = 0,0,0,0
# for _ in range(int(read())):
#     k = int(read())
#     s1, s2 = s2, k
#     a,b,c,d = b,c,d,max(c,b+s1)+s2
# print(d)