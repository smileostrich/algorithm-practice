def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            board[i-1].append((i-1)*columns+j)
    for x1,y1,x2,y2 in queries:
        tmp = board[x1-1][y2-1]
        min_val = 10001

        min_val = min(min(board[x1-1][y1-1:y2-1]), min_val)
        board[x1-1][y1:y2] = board[x1-1][y1-1:y2-1]

        for i in range(x1, x2):
            min_val = min(board[i][y1-1], min_val)
            board[i-1][y1-1] = board[i][y1-1]

    return answer