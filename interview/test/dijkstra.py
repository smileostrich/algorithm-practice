N = 100
INF = 100000
MAP = [[0] * (N + 1) for _ in range(N + 1)]
visit = [False] * (N + 1)
dist = [0] * (N + 1)


def dijkstra():
    global dist, visit, MAP
    v = 0
    dist[start] = 0

    for i in range(1, vertex + 1):
        min = INF
        for j in range(1, vertex + 1):
            if visit[j] == False and min > dist[j]:
                min = dist[j]
                v = j

        visit[v] = True

        for j in range(1, vertex + 1):
            if dist[j] > dist[v] + MAP[v][j]:
                dist[j] = dist[v] + MAP[v][j]


def main():
    global MAP, dist, visit, vertex, start

    T = int(input())

    for test_case in range(1, T + 1):
        vertex, start, end = map(int, input().split())
        edge = int(input())

        for i in range(1, vertex + 1):
            for j in range(1, vertex + 1):
                if i != j:
                    MAP[i][j] = INF

        for i in range(1, edge + 1):
            FROM, TO, value = map(int, input().split())
            MAP[FROM][TO] = value

        for i in range(1, vertex + 1):
            dist[i] = INF
            visit[i] = False

        dijkstra()
        print("#%d %d" % (test_case, dist[end]))


if __name__ == "__main__":
    main()