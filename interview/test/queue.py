queue = []


def queueInit():
    global queue
    queue.clear()


def queueIsEmpty():
    global queue
    return len(queue) == 0


def queueEnqueue(value):
    queue.append(value)


def queueDequeue():
    return queue.pop(0)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        queueInit()
        l = list(input().split())

        for i in l:
            queueEnqueue(i)

        print("#%d" % test_case, end=' ')

        while not queueIsEmpty():
            value = queueDequeue()
            if value != None:
                print(value, end=' ')

        print()


if __name__ == "__main__":
    main()