N = int(input())
li_matrix = [list(map(int,input().split())) for _ in range(N)]

white = 0
blue = 0

def recur(x,y,n):
    global white, blue
    chk = li_matrix[y][x]
    a = n//2
    for i in range(y, y+n):
        for j in range(x, x+n):
            if chk != li_matrix[i][j]:
                recur(x,y,a)
                recur(x+a, y, a)
                recur(x, y+a, a)
                recur(x+a, y+a, a)
                return
    if not chk:
        white += 1
        return
    else:
        blue += 1
        return
recur(0,0,N)
print(white)
print(blue)