# 분할정복으로 다시 풀기


a=int(input())
def s(n):
    if n==3:
        return['***','* *','***']
    x = s(n//3)
    y = list(zip(x,x,x))
    y = [''.join(y[i]) for i in range(len(y))]

    z = list(zip(x,[' '*(n//3)]*(n//3),x))
    z = [''.join(z[i]) for i in range(len(z))]

    return y+z+y
print('\n'.join(s(a)))