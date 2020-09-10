def mergeSort(kStr):
    if len(kStr) <= 3:
        return kStr
    mid = len(kStr) // 2
    # if mid == 1:
    if mid % 2 == 1:
        u = mergeSort(kStr[:mid-1])
        v = mergeSort(kStr[mid:])
    else:
        u = mergeSort(kStr[:mid])
        v = mergeSort(kStr[mid:])

    resultStr = ''
    re_u = strChk(u)
    re_v = strChk(v)
    if re_u and re_v:
        resultStr += u + v
        return resultStr
    if re_v:
        return '(' + v + ')' + u[-2:0:-1]
    if re_u:
        return v[::-1]



def strChk(chkStr):
    if chkStr[0] == ')':
        return False
    cnt = 1
    for i in chkStr[1:]:
        if cnt == -1:
            return False
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    if cnt != 0:
        return False
    return True


def solution(p):
    print(mergeSort(p))


solution(')())((')
# solution("(()())()")
solution(")(")
solution("()))((()")
