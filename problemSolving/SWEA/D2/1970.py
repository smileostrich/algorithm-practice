T = int(input())
for tc in range(1, T + 1):
    change = [0] * 8
    money = int(input())
    dic_change = {0:50000, 1:10000, 2:5000, 3:1000, 4:500, 5:100, 6:50, 7:10}
    for i in range(8):
        if money >= dic_change[i]:
            q, money = divmod(money, dic_change[i])
            change[i] += q
    print(f'#{tc}')
    print(*change)