# 인터넷 소스 (제곱근 까지만 구하면 됨)
# def isPrime(num):
#     if num==1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True
#
# M, N = map(int, input().split())
#
# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)


# 내소스 시간초과
import sys

M, N = map(int, sys.stdin.readline().split())
decimal_list = [2, 3]

for i in range(2, N+1):
    for j in decimal_list:
        if i % j == 0:
            break
        elif i % j != 0 and j == decimal_list[-1]:
            decimal_list.append(i)
            break

for i in decimal_list:
    if i >= M:
        print(i)