def solution(id_list, report, k):
    dic_name = {i:[0]*len(id_list) for i in id_list}
    li_result = [0]*len(id_list)
    dic_cmp = {v:k for k,v in enumerate(id_list)}
    for i in report:
        reporter, target = i.split()
        dic_name[target][dic_cmp[reporter]] = 1
    for i in dic_name.values():
        if sum(i) >= k:
            for idx, p in enumerate(i):
                li_result[idx] += p
    return li_result




print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))