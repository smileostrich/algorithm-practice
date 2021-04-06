T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    li_tree = [-1 for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        li_tree[a] = b
    for i in range(N,1,-1):
        if i%2 == 0 and li_tree[i//2] == -1:
            if i+1 <= N:
                li_tree[i//2] = li_tree[i] + li_tree[i + 1]
            else:
                li_tree[i // 2] = li_tree[i]
    print(f'#{test_case} {li_tree[L]}')