from sys import stdin


N, M = map(int, stdin.readline().rstrip().split())
arr = [0*n for n in range(12)]
li_isused = [0*n for n in range(12)]


def func(k):
    if k == M:
        for i in range(1, M+1):
            print(arr[i], end=" ")
        print("\n", end="")
        return 0
    for j in range(1, N+1):
        if li_isused[j] == False:
            if arr[k] > j:
                continue
            li_isused[j] = True
            arr[k+1] = j
            func(k+1)
            li_isused[j] = False


if __name__ == "__main__":
    func(0)