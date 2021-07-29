from collections import defaultdict

def solution(lottery):
    dic_person = defaultdict(int)
    dic_result = dict()
    for cur in lottery:
        if cur[1] == 1:
            if cur[0] not in dic_result:
                dic_result[cur[0]] = dic_person[cur[0]]+1
        else:
            dic_person[cur[0]] += 1
    if len(dic_result.keys()) == 0:
        return 0
    else:
        return sum(dic_result.values())//len(dic_result.keys())

# print(solution(	[[1, 0], [35, 0], [1, 0], [100, 1], [35, 1], [100, 1], [35, 0], [1, 1], [1, 1]]))
print(solution(	[[1, 0], [2, 0], [3, 0], [1, 0], [2, 0], [1, 0], [1, 1], [2, 0], [2, 0], [2, 1], [1, 0], [1, 1], [3, 0], [3, 0], [1, 1]]))