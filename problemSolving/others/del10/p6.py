def solution(board, skill):
    size_x = len(board[0])
    size_y = len(board)
    for s in skill:
        board2 = []
        type, y1,x1,y2,x2,damage = s
        for i in range(0,y1):
            board2.append([0]*size_x)
        for i in range(y1,y2+1):
            before = [0]*x1
            before.extend([damage] * (x2 - x1 + 1))
            if size_x-1 > x2:
                after = [0] * (size_x-1-x2)
                before.extend(after)
            board2.append(before)
        for i in range(y2+1,size_y):
            board2.append([0] * size_x)
        if type == 1:
            board = [[x-y for x,y in zip(a, b)] for a, b in zip(board, board2)]
        else:
            board = [[x+y for x, y in zip(a, b)] for a, b in zip(board, board2)]
    cnt = 0
    for i in board:
        for j in i:
            if j >= 1:
                cnt += 1
    return cnt


print(solution(	[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))