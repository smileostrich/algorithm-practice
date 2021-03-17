def binarySearch(arr, low, high, target):
    if low > high:
        print("-1", end=' ')
        return

    mid = (low + high) // 2

    if target < arr[mid]:
        binarySearch(arr, low, mid - 1, target)
    elif arr[mid] < target:
        binarySearch(arr, mid + 1, high, target)
    else:
        print(mid, end=' ')
        return


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        print("#%d" % test_case, end=' ')
        M = int(input())
        N = int(input())

        arr = list(map(int, input().split()))
        targetvalue = list(map(int, input().split()))

        for idx in range(N):
            binarySearch(arr, 0, M - 1, targetvalue[idx])
        print()


if __name__ == "__main__":
    main()