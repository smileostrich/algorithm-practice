def recur(idx, cnt, inner):
    global li_tri, high, N, li_max
    if li_max[idx] > idx
    if idx == N:
        if high < cnt:
            high = cnt
        return
    else:
        recur(idx+1, cnt+li_tri[idx][inner], inner)
        recur(idx + 1, cnt + li_tri[idx][inner], inner+1)


def solution(triangle):
    global li_tri, high, N, li_max
    li_max = [-1]*len(triangle)
    N = len(triangle)
    li_tri = triangle
    high = -1
    recur(0,0,0)
    return high


print(solution(	[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))