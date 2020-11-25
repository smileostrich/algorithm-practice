# import sys
#
# N = int(sys.stdin.readline())
# li = [0]*(2**(N-1))
# k = [''] * N
# k[0] = '1'
#
# for i in range(1, N):
#     for j in k[i-1]:
#         if j == '0':
#             k[i] = k[i] + '10'
#         elif j == '1':
#             k[i] = k[i] + '01'
#
# if N == 1:
#     print(0)
# elif N > 1:
#     if N % 2 == 0:
#         li[0] = 1
#         for idijhkljhx, i in enumerate(k[-1]):
#             if i == '0' and k[-1][idx - 1] == '1':
#                 li[idx] = li[idx-1] + 1
#             else:
#                 li[idx] = li[idx-1]
#     elif N % 2 == 1:
#         for idx, i in enumerate(k[-1]):
#             if i == '0' and k[-1][idx-1] == '1':
#                 li[idx] = li[idx-1] + 1
#             else:
#                 li[idx] = li[idx-1]
#
# print(li)
# # 0 1 1 3 5 11 21

# n=int(input())-1
# print((2**n-(-1)**n)//3)

arr = 1 >> 4
print(0b1101)