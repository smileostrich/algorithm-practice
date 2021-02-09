import heapq

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    h_asc = li
    heapq.heapify(h_asc)
    h_desc = []
    for i in li:
        heapq.heappush(h_desc, (-1*i,i))
    for i in range(N):
        h1,h2 = heapq.heappop(h_desc)
        heapq.heappush(h_desc, (h1+1, h2-1))
        heapq.heappush(h_asc, heapq.heappop(h_asc) + 1)
    print(f'#{test_case} {heapq.heappop(h_desc)[1] - heapq.heappop(h_asc)}')
