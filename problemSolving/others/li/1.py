# def solution(inp_str):
#     result = []
    if 8 <= len(inp_str) <= 15:
        result.append(1)
#     #3
#     # if
#
#     # 4
#     if inp_str
#     # 5
#
#     return result

def solution(table, languages, preference):
    dic_test = {}
    for i in range(5):
        li_tmp = list(table[i].split())
        dic_test[li_tmp[0]] = 0
        # lan/pre
        for l_idx in range(len(languages)):
            for t_idx in range(1, 6):
                if languages[l_idx] == li_tmp[t_idx]:
                    if t_idx == 1:
                        dic_test[li_tmp[0]] += preference[l_idx]*5
                    elif t_idx == 2:
                        dic_test[li_tmp[0]] += preference[l_idx]*4
                    elif t_idx == 3:
                        dic_test[li_tmp[0]] += preference[l_idx]*3
                    elif t_idx == 4:
                        dic_test[li_tmp[0]] += preference[l_idx]*2
                    elif t_idx == 5:
                        dic_test[li_tmp[0]] += preference[l_idx]*1
                    break
    high = max(dic_test.values())
    ans = []
    for idx,val in dic_test.items():
        if val == high:
            ans.append(idx)
    ans.sort()
    return ans[0]