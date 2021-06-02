dirfir = [(1,0),(0,1)]
dirsec = [(2,0),(0,2)]
dirthi = [(1,1)]
dirfou = [(-1,1)]


def bfs(li_bfs):
    for y in range(len(li_bfs)):
        for x in range(len(li_bfs)):
            if li_bfs[y][x] == 'P':
                for dx, dy in dirfir:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if li_bfs[ny][nx] == 'P':
                            return 0
                for dx, dy in dirsec:
                    if dx == 2:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if li_bfs[y][x + 1] != 'X' and li_bfs[ny][nx] == 'P':
                                return 0
                    else:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if li_bfs[y+1][x] != 'X' and li_bfs[ny][nx] == 'P':
                                return 0
                for dx, dy in dirthi:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if li_bfs[y][x + 1] == 'X' and li_bfs[y+1][x] == 'X':
                            continue
                        elif li_bfs[ny][nx] == 'P':
                            return 0
                for dx, dy in dirfou:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if li_bfs[y][x - 1] == 'X' and li_bfs[y+1][x] == 'X':
                            continue
                        elif li_bfs[ny][nx] == 'P':
                            return 0
    else:
        return 1


def solution(places):
    result = []
    for place in places:
        li_matrix = [list(i) for i in place]
        result.append(bfs(li_matrix))
    return result



print(solution([["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))