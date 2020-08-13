#dp 실패














# import sys
#
# A = int(sys.stdin.readline())
# n = list(map(int, sys.stdin.readline().split()))
# li = [0] * A
#
# for i in range(A):
#     for j in range(i):
#         if n[j] < n[i]:
#             li[i] = max(li[i], li[j]+1)
# print(max(li)+1)