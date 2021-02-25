T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        row = 0
        col = 0
        for j in range(9):
            row += matrix[j][i]
            col += matrix[i][j]
        if row != 45 or col != 45:
            result = 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            tmp = 0
            for k in range(3):
                for p in range(3):
                    tmp += matrix[j+p][i+k]
            if tmp != 45:
                result = 0
    print(f'#{tc} {result}')