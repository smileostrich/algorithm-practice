from collections import deque


def check(x,y,k):
    chk = arr[y][x]
    for ny in range(y,y+k):
        for nx in range(x,x+k):
            if arr[ny][nx] != chk:
                return -1
    else:
        return chk

def solution(test):
    global arr
    arr = test
    size = len(arr)
    s = 1
    dic_result = {}
    while s <= size:
        dic_result[s] = 0
        s *= 2
    size_sq = len(dic_result.keys())
    dq = deque([(1, size,0,0)])
    cnt_b = 0
    cnt_w = 0
    while dq:
        idx, s_cur,x,y = dq.popleft()
        if idx == size_sq:
            if arr[y][x] == 1:
                cnt_b += 1
            else:
                cnt_w += 1
        else:
            tmp = check(x, y, s_cur)
            if tmp == -1:
                dq.append((idx + 1, s_cur // 2, x, y))
                dq.append((idx + 1, s_cur // 2, x, y + s_cur//2))
                dq.append((idx + 1, s_cur // 2, x + s_cur//2, y))
                dq.append((idx + 1, s_cur // 2, x+s_cur//2, y+s_cur//2))
            elif tmp == 1:
                cnt_b += 1
            else:
                cnt_w += 1
    return [cnt_w, cnt_b]

print(solution(	[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))