N = int(input())
li_n = list(map(int, input().split()))

inc = [1]*N
desc = [1]*N

for i in range(N):
    for j in range(i):
        if li_n[j] < li_n[i]:
            inc[i] = max(inc[i],inc[j]+1)
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if li_n[j] < li_n[i]:
            desc[i] = max(desc[i],desc[j]+1)

result = [0 for i in range(N)]

for i in range(N):
    result[i] = inc[i] + desc[i] - 1
print(max(result))