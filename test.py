import unittest

import collections

test = defaultdict



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