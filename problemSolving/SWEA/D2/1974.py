T = int(input())
# T = 1
for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    # matrix = [list(map(int, '7 3 6 4 2 9 5 8 1'.split())),list(map(int, '5 8 9 1 6 7 3 2 4'.split())),list(map(int, '2 1 4 5 8 3 6 9 7'.split())),list(map(int, '8 4 7 9 3 6 1 5 2'.split())),list(map(int, '1 5 3 8 4 2 9 7 6'.split())),list(map(int, '9 6 2 7 5 1 8 4 3'.split())),list(map(int, '4 2 1 3 9 8 7 6 5'.split())),list(map(int, '3 9 5 6 7 4 2 1 8'.split())),list(map(int, '6 7 8 2 1 5 4 3 9'.split()))]
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