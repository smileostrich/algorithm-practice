import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li_load = [tuple(map(int, input().split())) for _ in range(N)]
    hq = []
    for s,e in li_load:
        heapq.heappush(hq, (e-s, s, e))
    cnt_load = 0
    cur_load = 0
    li_time = [False]*24
    while cur_load < len(li_load):
        val, cs, ce = heapq.heappop(hq)
        for k in range(cs, ce):
            if li_time[k]:
                break
        else:
            cnt_load += 1
            for i in range(cs, ce):
                li_time[i] = True
        cur_load += 1
    print(f'#{tc} {cnt_load}')
