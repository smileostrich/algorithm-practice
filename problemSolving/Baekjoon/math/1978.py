N = int(input())
li_p = list(map(int, input().split()))
li_cmp = [False, False] + [True]*(1000)
for i in range(2, int(len(li_cmp)**0.5)+1):
    if li_cmp[i]:
        for j in range(2*i, len(li_cmp), i):
            li_cmp[j] = False
cnt = 0
for i in li_p:
    if li_cmp[i]:
        cnt += 1
print(cnt)