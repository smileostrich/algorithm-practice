def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

N = int(input())
li_n = [int(input()) for _ in range(N)]
li_n.sort(reverse=True)
li_diff = []
li_ans = []
for i in range(1, N):
    li_diff.append(li_n[i] - li_n[i-1])

prev = li_diff[0]
for i in range(1, N):
    prev = gcd(prev, li_diff[i])
for i in range(2, int(prev**0.5) + 1):
    if prev % i == 0:
        li_ans.append(i)
        li_ans.append(prev//i)
li_ans.append(prev)
li_ans = list(set(li_ans))
li_ans.sort()
prev(*li_ans)
