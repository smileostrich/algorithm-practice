T = int(input())
for tc in range(1, T+1):
    sen = list(input())
    state = 1
    result = 0
    while True:
        cnt = 0
        de = []
        for i in sen:
            if de:
                if de[-1] == i:
                    de.pop()
                    cnt += 1
                else:
                    de.append(i)
            else:
                de.append(i)
        if cnt == 0:
            result = len(de)
            break
        else:
            sen = de
    print(f'#{tc} {result}')