import heapq

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    str_n = input()
    dic_n = {}
    h_n = []
    for i in str_n:
        i = int(i)
        if i in dic_n:
            dic_n[i] += 1
        else:
            dic_n[i] = 1
    for idx, val in dic_n.items():
        heapq.heappush(h_n,(-1*val,idx))
    v1, high = heapq.heappop(h_n)
    while True:
        if len(h_n) > 0:
            v2, tmp = heapq.heappop(h_n)
            if v1 == v2:
                if high < tmp:
                    high = tmp
            else:
                break
        else:
            break
    print(f'#{test_case} {high} {-1*v1}')