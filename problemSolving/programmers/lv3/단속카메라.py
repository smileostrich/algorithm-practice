def solution(routes):
    li_sort = sorted(routes, reverse=True)
    cur = 0
    cnt = 0
    while cur < len(routes):
        tmp = li_sort[cur][0]
        cur += 1
        for i in range(cur,len(li_sort)):
            s,e = li_sort[i]
            if e >= tmp >= s:
                cur += 1
                continue
            else:
                break
        cnt += 1
    return cnt


print(solution(	[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))