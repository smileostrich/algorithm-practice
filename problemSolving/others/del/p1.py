from itertools import combinations

def solution(names):
    dic_names = dict()

    for n in names:
        if n[0] in dic_names:
            dic_names[n[0]].append(n)
        else:
            dic_names[n[0]] = [n]
    dic_room1 = {i:[] for i in dic_names.keys()}
    dic_room2 = {i:[] for i in dic_names.keys()}
    for k,v in dic_names.items():
        for idx, i in enumerate(v):
            if idx % 2 == 0:
                dic_room1[k].append(i)
            else:
                dic_room2[k].append(i)
    cnt = 0
    for it in dic_room1.values():
        cnt += len(list(combinations(it,2)))
    for it in dic_room2.values():
        cnt += len(list(combinations(it,2)))
    return cnt


print(solution(["lemon", "lime", "werewolf", "wizard", "walnut"]))