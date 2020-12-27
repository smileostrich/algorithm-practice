from sys import stdin


# N, M = map(int, stdin.readline().rstrip().split())
N, M = 4, 4
arr = [0*i for i in range(10)]
isused = [0*i for i in range(10)]


def func(k):
    if k == M:
        for j in range(M):
            print(arr[j], end=' ')
        print('\n', end=' ')
        return 0
    for i in range(1, N + 1):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            func(k+1)
            isused[i] = False

if __name__ == "__main__":
    func(0)

