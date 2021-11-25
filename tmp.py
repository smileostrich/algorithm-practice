import sys
from itertools import combinations
sys.setrecursionlimit(2000)
import random


# def t1(t1,t2):
#     print(t1+t2)
#
# def t1(t1):
#     print(t1)
#
# t1(1,2)

# def lis(arr):
#     if not arr:
#         return 0
#
#     ret = 1
#     for i in range(len(arr)):
#         nxt = []
#         for j in range(i + 1, len(arr)):
#             if arr[i] < arr[j]:
#                 nxt.append(arr[j])
#         ret = max(ret, 1 + lis(nxt))
#     return ret
# print(lis([5,2,3]))

# class C:
#     def __init__(self, a1, a2):
#         self.a1 = a1
#         self.a2 = a2

    # def __hash__(self):
    #     return hash((self.a1, self.a2))
    #
    #
    # def __eq__(self, other):
    #     return (self.a1, self.a2) == (other.a1, other.a2)

# object_a = C("a", 1)
# object_b = C("a", 1)
# object_c = C("b", 2)
#
# a_dictionary = {object_a : 3, object_b : 4, object_c : 5}
# print(a_dictionary[object_a])

# dic_test = {1:'1vl',23:'2vl'}
# for i in dic_test:
#     print(i)

# def test(arr, r):
#     count = 0
#     dic_tmp = {}
#     dictPairs = {}
#
#     for i in reversed(arr):
#         if i*r in dictPairs:
#             count += dictPairs[i*r]
#         if i*r in dic_tmp:
#             dictPairs[i] = dictPairs.get(i, 0) + dic_tmp[i*r]
#
#         dic_tmp[i] = dic_tmp.get(i, 0) + 1
#
#     return count
# print(test([1,2,4],2))

# def minimumSwaps(arr):
#     ref_arr = sorted(arr)
#     index_dict = {v: i for i, v in enumerate(arr)}
#     swaps = 0
#
#     for i, v in enumerate(arr):
#         correct_value = ref_arr[i]
#         if v != correct_value:
#             to_swap_ix = index_dict[correct_value]
#             arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
#             index_dict[v] = to_swap_ix
#             index_dict[correct_value] = i
#             swaps += 1
#
#     return swaps
#
# print(minimumSwaps([7,1,3,2,4,5,6]))


# def largestRectangle(h):
#     # Write your code here
#     h += [0]
#     s = []
#     ma = 0
#     for i in range(0, len(h)):
#         j = i
#         while len(s) > 0 and s[-1][0] >= h[i]:
#             val, j = s.pop()
#             ma = max(ma, (i - j) * val)
#         s.append([h[i], j])
#     return ma
#
# print(largestRectangle([5,4,3,2,1]))

# def pre(num):
#     if num == 1:
#         return 0
#     if num % 2 == 0:
#         result = num // 2
#         return 1 + collatz(result)
#     else:
#         result = 3 * num + 1
#         return 1 + collatz(result)
#
#
# def collatz(num):
#     tmp = int(pre(num))
#     if tmp > 500:
#         return -1
#     else:
#         return tmp
# print(collatz(6))


# def lonely(n):
#     cnt = 0
#     result = []
#     while cnt < len(n):
#         current = n[cnt]
#         if current == n[cnt+1]:
#             result.append(current)
#             tmp = 1
#             while cnt+tmp < len(n):
#                 if current == n[cnt+tmp]:
#                     tmp += 1
#                 else:
#                     break
#             cnt += tmp
#         else:
#             result.append(current)
#             cnt += 1
#     return result
# print(lonely([1,1,3,3,0,1,1]))
# print(lonely([4,4,4,3,3]))


# li_pr = ['r1','r2', 'r3']
# print(li_pr[random.randrange(0,3)])
#
# print('123 456'.strip('1'))
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
