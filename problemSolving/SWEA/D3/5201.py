import heapq


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li_load = list(map(int, input().split()))
    li_truck = list(map(int, input().split()))
    hq = []
    for i in li_load:
        heapq.heappush(hq, (-i,i))
    li_truck.sort(reverse=True)
    result = 0
    cur_truck = 0
    tmp_hq = []
    while cur_truck < len(li_truck):
        if hq:
            tmp_hq.append(heapq.heappop(hq)[1])
            if tmp_hq[-1] <= li_truck[cur_truck]:
                result += tmp_hq[-1]
                cur_truck += 1
        else:
            break
    print(f'#{tc} {result}')
