def solution(rows, columns, queries):
    li_matrix = [[x+(y*columns)+1 for x in range(columns)] for y in range(rows)]
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    answer = []
    for query in queries:
        sy,sx,ey,ex = query
        sx,sy,ex,ey = sx-1,sy-1,ex-1,ey-1
        size = 2*(ex-sx+1)+2*(ey-sy+1)-4
        cnt = 0
        dir_cur = 0
        cx, cy = sx, sy
        last = li_matrix[cy][cx]
        lowest = last
        while cnt < size:
            dx, dy = dir[dir_cur]
            nx, ny = cx + dx, cy+ dy
            if sx <= nx <= ex and sy <= ny <= ey and 0<=nx<columns and 0<=ny<rows:
                cnt += 1
                if lowest > li_matrix[ny][nx]:
                    lowest = li_matrix[ny][nx]
                li_matrix[ny][nx], last = last, li_matrix[ny][nx]
                cx, cy = nx, ny
            else:
                dir_cur += 1
        answer.append(lowest)
    return answer



print(solution(3, 2, [[1, 1, 3, 2]]))
# print(solution(	3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))