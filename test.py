import unittest

# visited = [[[[False for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
# print(visited)
# visited[0][0][1][0] = True
# print(visited)
arr = [2, 4, 5, 8, 10, 11, 12, 13, 16, 17]
UNIT = 3
result = []
cur = arr[0]
for i in range(0, len(arr)):
    tmp = []
    result.append(arr[i:i+UNIT])
print(result)



# def make_tree(depth, level, flag):
#     global size
#     cnt = depth * 5
#     if depth < size:
#         dic_level[level].append(f'[str({li_tree[cnt+level]})]')
#         if cnt + level + 1 < size:
#             dic_level[level].append(f'--+--[{li_tree[cnt+level+1]}]')
#         else:
#             return
#         if cnt + level + 2 < size:
#             dic_level[level+1].append(f'       +--[{li_tree[cnt+level+2]}]')
#         else:
#             return
#         if cnt + level + 3 < size:
#             dic_level[level+2].append(f'       L--[{li_tree[cnt+level+3]}]')
#         else:
#             return
#         if cnt + level +  < size:
#             dic_level[level].append(f'-----[{li_tree[cnt+4]}]')
#             make_tree(cnt+6,level)
#         else:
#             return result[0] + result[1]+ result[2]
#         if cnt + 5 < size:
#             dic_level[2].append(f'-----[{li_tree[cnt + 5]}]')
#             result[2].append(make_tree(cnt+),level+1,'r')
#         else:
#             return ''.join(result[0]) + result[1]+ result[2]
#     return result
#
#
#
# li_tree = [1,2,3,4,5,6,7,8,9]
# dic_level = {}
# level = 0
# size = len(li_tree)
# make_tree(0)
# def tt(N):
#     test[-1] = N
#
# N = 999
# test = [1,2,3,4]
# tt(N)
# print(test)

# a = [1,2,3]
# b = a
# c = [1,2,3]
# print(a is b)
# print(a == b)
# print(b is c)
# print(b == c)
# print(eval(repr(123)))

# print(-7 % 3)

# print(5 and 3)
# a = [1,2,3,4,5,6,7]
# a[3 + 1:] = reversed(a[3 + 1:])
# a[::2] = [3,3,3,3]
# print(a)
# flask + terraform
# spinnaker (git hub 올리기)

# 라인 (dfs) 구현해보기
# dfs 문제 3개 남음 다풀어보기
# kmp 풀어보기
# string 관련 문제 완료
# def kmp:
#     test
#
# def kmp_matcher(li, d):
#     n = len(li)
#     m = len(d)
#
#     pi = compute_prefix_function(d)
#     q = 0
#     i = 0
#     while i < n:
#         if d[q] == li[i]:
#             q = q + 1
#             i = i + 1
#         else:
#             if q != 0:
#                 q = pi[q - 1]
#             else:
#                 i = i + 1
#         if q == m:
#             print
#             "pattern occurs with shift " + str(i - q)
#             q = pi[q - 1]
#
#
# def compute_prefix_function(p):
#     m = len(p)
#     pi = range(m)
#     k = 1
#     l = 0
#     while k < m:
#         if p[k] <= p[l]:
#             l = l + 1
#             pi[k] = l
#             k = k + 1
#         else:
#             if l != 0:
#                 l = pi[l - 1]
#             else:
#                 pi[k] = 0
#                 k = k + 1
#     return pi
#
#
# li = 'aaabc'
# p = 'aab'
# kmp_matcher(li, p)

# sec_stack = [1,2,3,4]
# sec_stack.sort()
# # print(sec_stack.index(3))
# test = sec_stack[sec_stack.index(3)+1:]
# sec_stack = sec_stack[:sec_stack.index(3)+1]
# print(test)
# print(sec_stack)
# tt = [1]
# while tt:
#     print(1)
#     tt.pop()
# import sys
# print(dict(map(lambda x: (int(x),[]), sys.stdin.readline().split())))

# import math
# from heapdict import heapdict
#
# test = heapdict()
# adjList = {'A': [('B', 10), ('C', 3)], 'B': [('C', 1), ('D', 2)], 'C': [('B', 4), ('D', 8), ('E', 2)], 'D': [('E', 7)], 'E': [('D', 9)]}
# vList = [2,3,4,5,1]
# pqueue = []
# d = d = {i:math.inf for i in vList}
# for v in vList:
#     heapdict.heappush(pqueue, [v, d[v]])
# print(pqueue)
# print(adjList['A'])
# for a,b in adjList['A']:
#     print(a,b)

# from collections import defaultdict
#
# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = defaultdict(lambda: [])
#
#     def add_edge(self, v, u, w):
#         self.graph[v].append((u, w))
#
#     def __str__(self):
#         result = ''
#         for v in self.V:
#             result += f'{v}: {str(self.graph[v])}, \n'
#         return result
#
#
# g = Graph(['A', 'B', 'C', 'D', 'E'])
# print(g.V)



# a = 4
# b = 3
# re = [4, 5]
# if a and b:
#     print('?')
# if b not in re:
#     print('b')
# if a and b not in re:
#     print('suc')


# print([1,2,3]*3)
#
#
# li = {(3,4):None,(1,2):(3,4)}
# def test(li, a, b, c):
#     tmp = li[(a, b)]
#     c += 1
#     if tmp != None:
#         return test(li, *tmp, c)
#     else:
#         return c
#
# print(test(li, 1,2,3))


# test = ['12345']
# print(test[0][1])


# li = [1,2,3]
# for i in range(5):
#     for j in range(5):
#         if j == 5 and i == 4:
#             break
#         print(j)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# from functools import reduce
#
# primes = [2, 3, 5, 7, 11, 13]
#
# def product(*numbers):
#     p = reduce(lambda x, y: x * y, numbers)
#     return p
# print(product(*primes));print(product(primes))

# for i in range(5, 0, -1):
#     print(i)

# print([0,0] + [1])
# print([0,0] + [1]*(3-1))

# test = {1:3,2:4}
# print(test.popitem())
# print(test.keys())

# current = 0
# for _ in range(0, 10):
#     current += 1

# print(current)
# def quicksort(x):
#     if len(x) <= 1:
#         return x
#
#     pivot = x[len(x) // 2]
#     less = []
#     more = []
#     equal = []
#     for a in x:
#         if a < pivot:
#             less.append(a)
#         elif a > pivot:
#             more.append(a)
#         else:
#             equal.append(a)
#
#     return quicksort(less) + equal + quicksort(more)
#
#
# list = [8, 13, 2, 6, 1, 4]
# quicksort(list)
#         # list = [8, 1, 2, 5, 10, 14, 7, 21]
#         # self.assertEqual([1, 2, 5, 7, 8, 10, 14, 21], quicksort(list)