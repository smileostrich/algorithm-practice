# def solution(gems):
#     size = len(set(gems))
#     dic = {gems[0]:1}
#     temp = [0, len(gems) - 1]
#     start, end = 0, 0
#
#     while(start < len(gems) and end < len(gems)):
#         if len(dic) == size:
#             if end - start < temp[1] - temp[0]:
#                 temp = [start, end]
#             if dic[gems[start]] == 1:
#                 del dic[gems[start]]
#             else:
#                 dic[gems[start]] -= 1
#             start += 1
#
#         else:
#             end += 1
#             if end == len(gems):
#                 break
#             if gems[end] in dic.keys():
#                 dic[gems[end]] += 1
#             else:
#                 dic[gems[end]] = 1
#
#     return [temp[0]+1, temp[1]+1]

def solutions(gems):
    set_gems = set(gems)
    dict_gemcnt = {keys:1 for keys in set_gems}
    start, end = 0, 0
    for gem in set_gems:
        c_lar= gems.index(gem)
        if c_lar > e:
            e = c_lar
    if s > gem:
        s += 1


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
