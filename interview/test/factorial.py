def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        value = factorial(num)
        print("#%d %d! = %d" % (test_case, num, value))


if __name__ == "__main__":
    main()