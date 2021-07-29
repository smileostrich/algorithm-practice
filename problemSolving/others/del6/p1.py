a = [1 for i in range(100)]
n = int(input())

def Print(t):
    print(n,'=',sep=' ',end='')
    for i in range(1,t):
        print(a[i],end='+')
    print(a[t])


def dfs(s,t):
    global n
    for i in range(a[t-1],s+1):
        if i<n:
            a[t] = i
            s -= i
            if s == 0:
                Print(t)
            else:
                dfs(s,t+1)
            s += i


dfs(n,1)