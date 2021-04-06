# def heapsort(a):
#     def swap(a,i,j):
#         a[i], a[j] = a[j], a[i]
#
#     def siftdown(a, i, size):
#         l = 2*i+1
#         r = 2*i+2
#         largest = i
#         if l <= size-1 and a[l] > a[i]:
#             largest = l
#         if r <= size-1 and a[r] > a[largest]:
#             largest = r
#         if largest != i:
#             swap(a, i, largest)
#             siftdown(a, largest, size)
#
#     def heapify(a, size):
#         p = (size//2)-1
#         while p >= 0:
#             siftdown(a, p, size)
#             p -= 1
#
#     size = len(a)
#     heapify(a, size)
#     end = size-1
#     while(end > 0):
#         swap(a, 0, end)
#         siftdown(a, 0, end)
#         end -= 1
#
# arr = [1,3,2,4,9,7]
# heapsort(arr)
# print(arr)

import heapq


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li_tree = []
    for i in list(map(int, input().split())):
        heapq.heappush(li_tree, i)
    i = N // 2
    cnt = 0
    while i > 0:
        cnt += li_tree[i-1]
        i = i // 2
    print(f'#{test_case} {cnt}')