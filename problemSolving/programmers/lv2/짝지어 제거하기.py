def solution(s):
    cmp = list(s)
    tmp = [cmp[0]]
    size = len(cmp)

    for i in range(1, size):
        if tmp:
            if tmp[-1] == cmp[i]:
                tmp.pop()
            else:
                tmp.append(cmp[i])
        else:
            tmp.append(cmp[i])
    if tmp:
        flag = True
        while flag:
            flag = False
            if tmp:
                cmp = tmp
                tmp = [cmp[0]]
                size = len(cmp)
                for i in range(1, size):
                    if tmp:
                        if tmp[-1] == cmp[i]:
                            tmp.pop()
                            flag = True
                        else:
                            tmp.append(cmp[i])
                    else:
                        tmp.append(cmp[i])
            else:
                return 1
        return 0
    else:
        return 1

print(solution("baabaa"))