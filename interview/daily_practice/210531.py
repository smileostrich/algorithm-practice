def factorial(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        t1, t2 = factorial(n - 2), factorial(n-1)
        # print(t1, t2)
        return t1+t2

print(factorial(7))
# 0 1 1 2 3 5 8 13

def reverse(li):
    return list(zip(*reversed(li)))


def reverse2(li):
    r = len(li)
    c = len(li[0])
    result = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            result[j][r-i-1] = li[i][j]
    return result


def reverse3(li):
    s = len(li)
    li_re = [[0]*s for i in range(s)]
    for y in range(s):
        for x in range(s):
            li_re[x][s-1-y] = li[y][x]
    return li_re


print(reverse([[1,2,3],[4,5,6],[7,8,9]]))
print(reverse2([[1,2,3],[4,5,6],[7,8,9]]))
print(reverse3([[1,2,3],[4,5,6],[7,8,9]]))
# 1 2 3   7 4 1
# 4 5 6   8 5 2
# 7 8 9   9 6 3