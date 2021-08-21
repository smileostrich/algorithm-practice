N = int(input())
def dfs(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        dfs(n-1,a,c,b)
        print(a,c)
        dfs(n-1,b,a,c)
sum = 1
for i in range(N-1):
    sum = sum*2+1
print(sum)
dfs(N,1,2,3)