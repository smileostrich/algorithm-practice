import heapq


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li_tree = []
    for i in list(map(int, input().split())):
        heapq.heappush(li_tree, i)
    i = N // 2
    cnt = 0
    while i > 0:
        cnt += li_tree[i-1]
        i = i // 2
    print(f'#{test_case} {cnt}')