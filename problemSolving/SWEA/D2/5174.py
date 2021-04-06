from collections import deque


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    li_tree = list(map(int, input().split()))
    dic_tree = {i:[] for i in range(1,E+2)}
    for i in range(0,len(li_tree),2):
        dic_tree[li_tree[i]].append(li_tree[i+1])
    dq = deque([N])
    visited = [False for i in range(E+2)]
    cnt = 1
    while dq:
        cur = dq.popleft()
        for i in dic_tree[cur]:
            if not visited[i]:
                dq.append(i)
                cnt += 1
        visited[cur] = True
    print(f'#{test_case} {cnt}')
