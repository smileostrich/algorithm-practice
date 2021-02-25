T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    for i in range(0,N//2+1):
        for j in range(N//2-i, N//2+i+1):
            result += matrix[i][j]
    for i in range(1, N//2+1):
        for j in range(i, N-i):
            result += matrix[N//2+i][j]
    print(f'#{tc} {result}')