import math


def solution(str1, str2):
    set1 = set()
    set2 = set()
    li_set1 = {}
    li_set2 = {}
    for i in range(0,len(str1)-1):
        tmp = str1[i:i+2]
        if tmp.isalpha() and len(tmp) == 2:
            tmp = tmp.lower()
            set1.add(tmp)
            if tmp in li_set1:
                li_set1[tmp] += 1
            else:
                li_set1[tmp] = 1
    for i in range(0,len(str2)-1):
        tmp2 = str2[i:i+2]
        if tmp2.isalpha() and len(tmp2) == 2:
            tmp2 = tmp2.lower()
            set2.add(tmp2)
            if tmp2 in li_set2:
                li_set2[tmp2] += 1
            else:
                li_set2[tmp2] = 1
    ins = set1.intersection(set2)
    union = set1.union(set2)
    c_ins = 0
    c_union = 0
    for n in ins:
        c_ins += min(li_set1[n], li_set2[n])
    for n in union:
        r1, r2 = 0, 0
        if li_set1.get(n):
            r1 = li_set1[n]
        if li_set2.get(n):
            r2 = li_set2[n]
        c_union += max(r1, r2)
    if not c_ins and not c_union:
        return 65536
    return int(math.floor(c_ins/c_union*65536))

print(solution("aa1+aa2", "AAAA12"))