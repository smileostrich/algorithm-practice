T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li_no = []
    for _ in range(N):
        li_no.append(tuple(map(int, input().split())))
    p = int(input())
    li_c = [int(input()) for _ in range(p)]
    li_re = [0]*(5000+1)
    for a,b in li_no:
        for i in range(a,b+1):
            li_re[i] += 1
    result = []
    for i in li_c:
        result.append(li_re[i])
    print(f"#{test_case}", *result)