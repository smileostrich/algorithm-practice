
def bfs(subin, sister):
    frontier = [subin]
    visited = [[False]*500001 for _ in range(2)]
    visited[0][subin] = True
    flag = 0
    time = 0
    while frontier:
        if sister > 500000:
            break
        if visited[flag][sister] == True:
            return time
        next = []
        flag = 1 - flag
        for cur_subin in frontier:
            for neighbor in (cur_subin-1, cur_subin+1, cur_subin*2):
                if 0 <= neighbor <= 500000 and visited[flag][neighbor] == False:
                    visited[flag][neighbor] = True
                    next.append(neighbor)
        time += 1
        frontier = next
        sister += time
    return -1

subin, sister = map(int, input().split())
print(bfs(subin,sister))