M = int(input())
N = int(input())
s = 0
f = 10001
m = max(M,N)
li_pr = [False,False] + [True]*(m)
for i in range(m):
    if li_pr[i]:
        for j in range(2*i, m+1, i):
            if li_pr[j]:
                li_pr[j] = False
for i in range(min(M,N),m+1):
    if li_pr[i]:
        s += i
        if f > i:
            f = i
if s == 0:
    print(-1)
else:
    print(s)
    print(f)