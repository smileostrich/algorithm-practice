from copy import deepcopy
def go(prev_dir, cy, cx, grid, d, cnt):
    if cy < 0 or cy >= len(grid) or cx < 0 or cx >=2*cy+1:
        return cnt
    if d[cy][cx][prev_dir] != -1:
        return d[cy][cx][prev_dir]
    ret = d[cy][cx][prev_dir]
    print(grid[cy][cx])
    if prev_dir == 0:
        if grid[cy][cx] == 'R':
            if cx % 2 == 0:
                ret = max(ret, go(2,cy+1,cx+1,grid,d,cnt+1))
            else:
                ret = max(ret, go(0,cy,cx+1,grid,d,cnt+1))
        elif grid[cy][cx] == 'B':
            if cx % 2 == 0:
                ret = max(ret, go(0,cy,cx+1,grid, d, cnt+1))
            else:
                ret = max(ret, go(3, cy-1, cx-1, grid, d, cnt+1))
    elif prev_dir == 1:
        if grid[cy][cx] == 'R':
            if cx % 2 == 0:
                ret = max(ret, go(1, cy, cx-1, grid, d, cnt+1))
            else:
                ret = max(ret,go(3, cy-1, cx-1, grid, d, cnt+1))
        elif grid[cy][cx] == 'B':
            if cx %2 == 0:
                ret = max(ret, go(2,cy+1,cx+1, grid, d, cnt+1))
            else:
                ret = max(ret, go(1, cy, cx-1, grid, d, cnt+1))
    elif prev_dir == 2:
        if grid[cy][cx] == 'R':
            ret = max(ret, go(1,cy,cx-1, grid, d, cnt+1))
        elif grid[cy][cx] == 'B':
            ret = max(ret, go(0,cy,cx+1,grid,d,cnt+1))
    else:
        if grid[cy][cx] == 'R':
            ret = max(ret, go(0,cy,cx+1, grid, d, cnt+1))
        elif grid[cy][cx] == 'B':
            ret = max(ret, go(1, cy, cx-1, grid,d,cnt+1))
    d[cy][cx][prev_dir] = ret
    return ret

def solution(grid):
    answer = 0
    size = len(grid)
    d = [[[-1 for _ in range(4)] for _ in range(2*size+1)] for _ in range(2*size+1)]
    # print(d)
    for i in range(size):
        answer = max(answer, go(0, i, 0, grid, deepcopy(d), 0))
        answer = max(answer, go(1, i, 2*i, grid, deepcopy(d), 0))
    for j in range(2*size+1):
        answer = max(answer, go(3,size-1,j,grid,deepcopy(d),0))
    return answer

print(solution(["R","BBB","RBRBR"]))