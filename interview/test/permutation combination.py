combinationStack = []


def printString(cArr):
    for i in cArr:
        print(i, end='')
    print()


def swap(cArr, x, y):
    cArr[x], cArr[y] = cArr[y], cArr[x]


def permutation(cArr, l, r):
    if l == r:
        printString(cArr)
    else:
        for i in range(l, r + 1, 1):
            swap(cArr, l, i)
            permutation(cArr, l + 1, r)
            swap(cArr, l, i)


def push(ch):
    combinationStack.append(ch)


def pop():
    combinationStack.pop()


def combination(cArr, length, offset, k):
    if k == 0:
        printString(combinationStack)
    else:
        for i in range(offset, length - k + 1, 1):
            push(cArr[i])
            combination(cArr, length, i + 1, k - 1)
            pop()


def main():
    global cArr, N, K
    T = int(input())

    for test_case in range(1, T + 1):
        cArr = list(input())

        N = int(input())
        K = int(input())

        print("#%d" % test_case)

        permutation(cArr[0:N], 0, N - 1)
        combination(cArr, N, 0, K)


if __name__ == "__main__":
    main()