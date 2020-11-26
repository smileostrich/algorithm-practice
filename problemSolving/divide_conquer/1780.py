import sys
import pprint
inp = lambda : sys.stdin.readline().rstrip()

N = int(inp())
mat = [list(map(int, inp().split())) for _ in range(N)]

def divid(arr):
    a=b=c=0
    l=len(arr)
    if l == 3:
        for i in range(3):
            for j in range(3):
                if arr[i][j] == -1:
                    a+=1
                elif arr[i][j] == 0:
                    b+=1
                else:
                    c+=1
        if a == 9 or b == 9 or c == 9:
            return a%8, b%8, c%8
        return a, b, c
    for i in range(0,l,l//3):
        for j in range(0,l,l//3):
            tmp = []
            for k in range(l//3):
                tmp.append(arr[i+k][j:j+l//3])
            tmp1,tmp2,tmp3=divid(tmp)
            a+=tmp1
            b+=tmp2
            c+=tmp3
    if a+b==0 or b+c==0 or a+c==0:
        return a%8, b%8, c%8
    return a, b, c

pprint.pprint(divid(mat), width=50)
# for i in divid(mat):
#     print(i)


# from itertools import product
# input=__import__('sys').stdin.readline
# n = int(input())
# l = [input().split() for i in range(n)]
# dict = {'-1':0,'0':0,'1':0}
# def check(x,y,n):
#     k = l[y+0][x+0]
#     for i, j in product(range(n),range(n)):
#         if l[y+i][x+j]!=k: return False
#     return True
# def f(x,y,n):
#     if n==1 or check(x,y,n): dict[l[y][x]]+=1; return
#     z = n//3
#     f(x, y, z)
#     f(x, y+z, z)
#     f(x, y+2*z, z)
#     f(x+z, y, z)
#     f(x+z, y+z, z)
#     f(x+z, y+2*z, z)
#     f(x+2*z, y, z)
#     f(x+2*z, y+z, z)
#     f(x+2*z, y+2*z, z)
# f(0,0,n)
# print(dict['-1'])
# print(dict['0'])
# print(dict['1']