from itertools import combinations

def solution(clothes):
    dic_clothes = dict()
    tmp = list(zip(*clothes))
    for i in tmp[1]:
        dic_clothes[i] = []
    for sp in clothes:
        a,b = sp
        dic_clothes[b].append(a)
    cnt = 1
    for t in dic_clothes:
        cnt *= len(dic_clothes[t]) + 1
    # for i in range(1, len(dic_clothes.keys())+1):
    #     for c in combinations(dic_clothes.keys(),i):
    #         mul = 1
    #         for inner in c:
    #             mul *= len(dic_clothes[inner])
    #         cnt += mul
    return cnt - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))