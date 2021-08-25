li_n = [0 for _ in range(101)]
li_n[1] = li_n[2] = li_n[3] = 1
for i in range(4,101):
    li_n[i] = li_n[i-2] + li_n[i-3]
T = int(input())
for _ in range(T):
    N = int(input())
    print(li_n[N])