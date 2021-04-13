T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    flag = 0
    for i in range(1,13):
        tmp = N - pow(2, -1 * i)
        if tmp > 0:
            result += '1'
            N = tmp
        elif tmp == 0:
            result += '1'
            flag = 1
            break
        else:
            result += '0'
    if not flag:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')