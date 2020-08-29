# 3시간..... ㅠㅜㅜㅠㅠㅠㅠㅠ

# 내가짠거 + 인터넷 보고 리팩토링
import sys

def bfs(queue):
    k = 0
    while queue:
        next = []
        for a, b in queue:
            for dx, dy in near:
                newX, newY = a+dx, b+dy
                if (0 <= newY < N) and (0 <= newX < M) and (mat[newY][newX] == 0):
                    next.append((newX, newY))
                    mat[newY][newX] = 1
        queue = next
        k += 1

    for i in mat:
        if 0 in i:
            return -1
    return k-1


M, N = map(int, sys.stdin.readline().split())
mat = [[] for _ in range(N)]
near = [(1, 0), (0, 1), (0, -1), (-1, 0)]
queue = []
for i in range(N):
   mat[i] = list(map(int, sys.stdin.readline().split()))
   for idxj, j in enumerate(mat[i]):
       if j == 1:
           queue.append((idxj,i))
print(bfs(queue))



# 내가 짠 소스
4# import sys
#
# def bfs(adj):
#     queue = []
#     for i in adj:
#         queue.append(i)
#     global k
#
#     while queue:
#         next = []
#         for a, b in queue:
#             for dx, dy in near:
#                 newX, newY = a+dx, b+dy
#                 # if newX < 0 or newX >= M or newY < 0 or newY >= N or mat[newY][newX] == -1 or mat[newY][newX] == 1 or (newX, newY) in queue:
#                 #     continue
#                 # elif mat[newY][newX] == 0:
#                 if (0 <= newY < N) and (0 <= newX < M) and (mat[newY][newX] == 0):
#                     next.append((newX, newY))
#                     mat[newY][newX] = 1
#         queue = next
#         k += 1
#     return k
#
#
# M, N = map(int, sys.stdin.readline().split())
# mat = [[] for _ in range(N)]
# near = [(1, 0), (0, 1), (0, -1), (-1, 0)]
# adj = []
# for i in range(N):
#    mat[i] = list(map(int, sys.stdin.readline().split()))
#    for idxj, j in enumerate(mat[i]):
#        if j == 1:
#            adj.append((idxj,i))
# k = 0
# largest = 0
#
# bfs(adj)
# largest = k - 1
#
# for i in mat:
#     i.sort()
#     for j in range(M):
#         ts = i[j]
#         if ts == -1:
#             continue
#         elif ts == 1:
#             break
#         elif ts == 0:
#             largest = -1
#             break
#     if largest == -1:
#         break
# print(largest)
