from itertools import combinations
from collections import Counter

def check(sa, sb):
    resa,a = sa
    resb,b = sb

    if a == b:
        return sa
    elif a==1 and b==2:
        return sa
    elif a==1 and b==3:
        return sb
    elif a==2 and b==1:
        return sb
    elif a==2 and b==3:
        return sa
    elif a==3 and b==1:
        return sa
    elif a==3 and b==2:
        return sb

def competition(race):
    race = [(idx,val) for idx, val in enumerate(map(int, race.split()))]
    winner = []
    loser = []
    for inner in range(0,len(race)-1,4):
        tmp_dic = []
        for val in list(combinations(race[inner:inner + 4],2)):

            tmp_dic.append(check(*val))
        res = Counter(tmp_dic).most_common(2)
        winner.append(res[0][0])
        loser.append(res[1][0])
    l16 = []
    for a,b in zip(winner,reversed(loser)):
        l16.append(check(sorted([a,b])))
    l8 = []
    for inner in range(0,7,2):
        l8.append(check(*l16[inner:inner+2]))
    l4 = []
    for inner in range(0, 3, 2):
        l4.append(check(*l8[inner:inner + 2]))
    return check(*l4)[0]

T = int(input())
for t in range(1, T+1):
    inp = input()
    print(f'#{t} {competition(inp)}')