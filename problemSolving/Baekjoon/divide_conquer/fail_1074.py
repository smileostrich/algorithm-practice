# import sys
#
# result = 0
#
#
# def z(n, x, y):
#     global result
#     if x == r and y == c:
#         print(int(result))
#         exit(0)
#
#     if n == 1:
#         result += 1
#         return
#
#     if not (x <= r < x + n and y <= c < y + n):
#         result += n * n
#         return
#     z(n / 2, x, y)
#     z(n / 2, x, y + n / 2)
#     z(n / 2, x + n / 2, y)
#     z(n / 2, x + n / 2, y + n / 2)
#
#
# n, r, c = map(int, sys.stdin.readline().split(' '))
# z(2 ** n, 0, 0)



def f(N, r, c):
    if N == 0:
        return 0
    M = 2 ** (N-1)
    cnt = 0
    if r >= M:
        cnt += 4 ** N // 2
    if c >= M:
        cnt += 4 ** N // 4
    return f(N-1, r%M, c%M) + cnt


N, r, c = map(int, input().split())

print(f(N, r, c))
