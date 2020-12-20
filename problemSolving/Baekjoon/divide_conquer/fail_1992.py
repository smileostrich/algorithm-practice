X = int(input())
mat = [input() for _ in range(X)]


def quad(x, y, n):
    if n == 1:
        return mat[y][x]

    a = n // 2

    r1 = quad(x, y, a)
    r2 = quad(x + a, y, a)
    r3 = quad(x, y + a, a)
    r4 = quad(x + a, y + a, a)

    if r1 == r2 == r3 == r4 and len(r1) == 1:
        return r1

    return "(" + r1 + r2 + r3 + r4 + ")"


print(quad(0, 0, X))