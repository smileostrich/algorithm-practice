stack = []


def stackInit():
    global stack
    stack.clear()


def stackIsEmpty():
    global stack
    return len(stack) == 0


def stackPush(value):
    stack.append(value)


def stackPop():
    return stack.pop()


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        stackInit()

        l = list(input().split())

        for i in l:
            stackPush(i)

        print("#%d" % test_case, end=' ')

        while not stackIsEmpty():
            value = stackPop()
            if value != None:
                print(value, end=' ')

        print()


if __name__ == "__main__":
    main()