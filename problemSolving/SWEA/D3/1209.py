T = int(10)
for tc in range(1, T + 1):
    t = input()
    result = []
    matrix = []
    for _ in range(100):
        tmp = list(map(int, input().split()))
        result.append(sum(tmp))
        matrix.append(tmp)
    for i in range(100):
        t_sum = 0
        dae_1 = 0
        dae_2 = 0
        for j in range(100):
            t_sum += matrix[j][i]
            if i == j:
                dae_1 += matrix[i][j]
            if i+j == 100:
                dae_2 += matrix[i][j]
        result.append(t_sum)
        result.append(dae_1)
        result.append(dae_2)
    print(f'#{tc} {max(result)}')