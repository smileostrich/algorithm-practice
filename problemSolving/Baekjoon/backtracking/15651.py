from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
li_arr = [0] * (N+1)
bool_isused = [0] * (N+1)


def test(k):
    if k == M:
        for i in range(1, M+1):
            print(li_arr[i], end=' ')
        print('\n', end='')
        return 0
    for j in range(1, N+1):
            li_arr[k+1] = j
            test(k+1)


if __name__ == '__main__':
    test(0)
