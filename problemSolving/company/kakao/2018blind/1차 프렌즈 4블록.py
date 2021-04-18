from collections import deque

def solution(m, n, li_tmp):
    board = []
    for i in li_tmp:
        board.append(list(i))
    cnt = 0
    while True:
        box = []
        for y in range(0,m-1):
            for x in range(0,n-1):
                tmp = set()
                for dy in range(2):
                    for dx in range(2):
                        tmp.add(board[y+dy][x+dx])
                if len(tmp) == 1 and list(tmp)[0] != 0:
                    box.append((x,y))
        if len(box) == 0:
            break
        else:
            for vx,vy in box:
                for dy in range(2):
                    for dx in range(2):
                        if board[vy+dy][vx+dx] != 0:
                            board[vy + dy][vx + dx] = 0
                            cnt += 1
            for y in range(m-1, 0, -1):
                for x in range(n - 1, -1, -1):
                    if board[y][x] == 0:
                        for nz in range(y-1,-1,-1):
                            if board[nz][x] != 0:
                                board[y][x], board[nz][x] = board[nz][x], 0
                                break
    return cnt


print(solution(	4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))