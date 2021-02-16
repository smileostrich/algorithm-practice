for tc in range(1,11):
    t = input()
    matrix = []
    for i in range(99):
        matrix.append(list(map(int, input().split())))
    lastline = list(map(int, input().split()))
    matrix.append(lastline)

    cur = lastline.index(2)
    for i in range(99,-1,-1):
        if 0 <= cur - 1 < 100 and matrix[i][cur - 1] == 1:
            cur -= 1
            while True:
                if 0<=cur-1<100 and matrix[i][cur-1] == 1:
                    cur -= 1
                else:
                    break
        elif 0<=cur+1<100 and matrix[i][cur+1] == 1:
            cur += 1
            while True:
                if 0<=cur+1<100 and matrix[i][cur+1] == 1:
                    cur += 1
                else:
                    break
        else:
            continue
    print(f'#{tc} {cur}')