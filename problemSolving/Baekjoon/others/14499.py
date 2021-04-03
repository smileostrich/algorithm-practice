N,M,y,x,size_order = map(int, input().split())
li_matrix = [list(map(int, input().split())) for _ in range(N)]
li_move = list(map(int, input().split()))
dice = {1:0,2:0,3:0,4:0,5:0,6:0}
# 1 동 2 서 3 북 4 남
dict_dir = {1:[1,0],2:[-1,0],3:[0,-1],4:[0,1]}

for face in li_move:
    cx, cy = dict_dir[face]
    nx, ny = x+cx, y+cy

    if 0 <= nx < M and 0 <= ny < N:
        # 동
        if face == 1:
            dice[3], dice[1], dice[4], dice[6] = dice[1], dice[4], dice[6], dice[3]
        # 서
        elif face == 2:
            dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
        # 북
        elif face == 3:
            dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
        # 남
        else:
            dice[6], dice[5], dice[1], dice[2] = dice[5], dice[1], dice[2], dice[6]
        print(dice[1])
        if li_matrix[ny][nx] == 0:
            li_matrix[ny][nx] = dice[6]
        else:
            dice[6], li_matrix[ny][nx] = li_matrix[ny][nx], 0
        x, y = nx, ny
