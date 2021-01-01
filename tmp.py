import sys
from itertools import combinations

num1 = 1
num2 = 2
def swap(num1, num2):
    tmp = num1
    num1 = num2
    num2 = tmp
    return num1, num2
swap(num1,num2)
print(num1, num2)

# In = sys.stdin.readline
#
# n = int(In())
# meetings = [(*map(int, In().split()),) for _ in range(n)]
# print(meetings)
# meetings.sort()
# print(meetings)

# print(float('inf'))
# print([i for i in reversed(range(7//2))])
# print([i for i in range(7//2-1, -1, -1)])

# testList = []
#
#
# # zip
# p1 = zip([1,2,3,4], [2,3,4,5])
# # 범위 중에서 홀수만
# p2 = list(filter(lambda x: x%2 == 1, [1,2,3,4,5]))
#
#
#
# testList.append(p1)
# testList.append(p2)
# testList.append(p3)
# testList.append(p4)
# testList.append(p5)
# for i in testList:
#     print(i)


# import sys
#
# def bfs(queue):
#     k = 0
#     while queue:
#         next = []
#         for a, b in queue:
#             for dx, dy in near:
#                 newX, newY = a+dx, b+dy
#                 if (0 <= newY < N) and (0 <= newX < M) and (mat[newY][newX] == 0):
#                     next.append((newX, newY))
#                     mat[newY][newX] = 1
#         queue = next
#         k += 1
#
#     for i in mat:
#         if 0 in i:
#             return -1
#     return k-1
#
#
# M, N = map(int, sys.stdin.readline().split())
# mat = [[] for _ in range(N)]
# near = [(1, 0), (0, 1), (0, -1), (-1, 0)]
# queue = []
# for i in range(N):
#    mat[i] = list(map(int, sys.stdin.readline().split()))
#    for idxj, j in enumerate(mat[i]):
#        if j == 1:
#            queue.append((idxj,i))
# print(bfs(queue))
