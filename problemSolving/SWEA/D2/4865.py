T = int(input())
for tc in range(1, T+1):
    sor = set(list(input()))
    tar = input()

    dic_res = {i:0 for i in sor}
    for k in sor:
        for j in tar:
            if k == j:
                dic_res[k] += 1

    print(f'#{tc} {max(dic_res.values())}')