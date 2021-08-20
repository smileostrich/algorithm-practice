M, N, H = map(int, input().split())
li_matrix = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        li_matrix[i].append(list(map(int, input().split())))
for i in range(H):
    for j in range(N):
        for k in range(M):
            if li_matrix[i][j][k] == 0:
                print(-1)
                exit(0)