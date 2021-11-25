mod = 1000000007
import sys
sys.setrecursionlimit(10000000)

def right(s, i, n, x, y):
    if n < x or x < 0 or i >= len(s):
        return 0
    if s[i] == 'r':
        x += 1
        i += 1
        return (1 if x==y else 0) + right(s,i,n,x,y) % mod + left(s,i,n,x,y) % mod
    i += 1
    return right(s, i, n, x, y) % mod

def left(s, i, n, x, y):
    if n < x or x < 0 or i >= len(s):
        return 0
    if s[i] == 'l':
        x -= 1
        i += 1
        return (1 if x==y else 0) + left(s,i,n,x,y) % mod + right(s,i,n,x,y) % mod
    i += 1
    return left(s,i,n,x,y) % mod

def distinctMoves(s, n, x, y):
    return ((1 if x == y else 0) + right(s, 0, n, x, y) + left(s, 0, n, x, y)) % mod

print(distinctMoves('rrlrlr',6,1,2))