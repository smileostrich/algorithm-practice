T = int(input())
for tc in range(1, T+1):
    mycard = input()
    li_card = []
    S = 0
    D = 0
    H = 0
    C = 0
    for i in range(0,len(mycard),3):
        li_card.append(mycard[i:i+3])
    if len(set(li_card)) != len(li_card):
        print(f'#{tc} ERROR')
    else:
        for i in li_card:
            if i[0] == 'S':
                S += 1
            elif i[0] == 'H':
                H += 1
            elif i[0] == 'D':
                D += 1
            else:
                C += 1
        print(f'#{tc} {13-S} {13-D} {13-H} {13-C}')



