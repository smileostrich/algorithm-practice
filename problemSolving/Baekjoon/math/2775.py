T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    li_m = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, n+1):
        li_m[0][i] = i
    for j in range(1, k+1):
        for i in range(1, n+1):
            li_m[j][i] = sum(li_m[j-1][:i+1])
    print(li_m[-1][-1])


