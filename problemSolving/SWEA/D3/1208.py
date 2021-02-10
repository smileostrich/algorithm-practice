import heapq

# way 1
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
T = 10

# way 2
for t in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # 가로 길이는 항상 100
    for i in range(dump):
        boxes.sort()
        boxes[0] += 1
        boxes[99] -= 1
    boxes.sort()
    res = boxes[99] - boxes[0]
    print(f'#{t} {res}')

# way 3
def min_max(li):
    max_v = 0
    max_idx = 0
    min_v = 101
    min_idx = 0
    for i in range(len(li)):
        if li[i] > max_v:
            max_v = li[i]
            max_idx = i
        if li[i] < min_v:
            min_v = li[i]
            min_idx = i
    return max_v, max_idx, min_v, min_idx


for tc in range(1, 11):
    dump = int(input())
    li = list(map(int, input().split()))
    for _ in range(dump):
        max_v, max_idx, min_v, min_idx = min_max(li)
        li[max_idx] -= 1
        li[min_idx] += 1
        dump -= 1
    max_v, max_idx, min_v, min_idx = min_max(li)
    print('#{} {}'.format(tc, max_v - min_v))