MAX_SIZE = 100
heapSize = 0
heap = list()


def heapInit():
    global heapSize, heap
    heap.clear()
    for i in range(MAX_SIZE):
        heap.append(0)


def heapPush(value):
    global heapSize, heap
    if heapSize + 1 > MAX_SIZE:
        return
    heap[heapSize] = value

    current = heapSize
    while current > 0 and heap[current] < heap[(current - 1) // 2]:
        heap[(current - 1) // 2], heap[current] = heap[current], heap[(current - 1) // 2]
        current = (current - 1) // 2

    heapSize = heapSize + 1


def heapPop():
    global heapSize, heap

    if heapSize <= 0:
        return -1

    value = heap[0]
    heapSize = heapSize - 1

    heap[0] = heap[heapSize]

    current = 0
    while current < heapSize and current * 2 + 1 < heapSize:
        child = 0
        if current * 2 + 2 >= heapSize:
            child = current * 2 + 1
        else:
            if heap[current * 2 + 1] < heap[current * 2 + 2]:
                child = current * 2 + 1
            else:
                child = current * 2 + 2

        if heap[current] < heap[child]:
            break

        heap[current], heap[child] = heap[child], heap[current]
        current = child

    return value


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        heapInit()

        value = list(map(int, input().split()))

        for i in range(N):
            heapPush(value[i])

        print("#%d" % test_case, end=' ')
        for i in range(N):
            print(heapPop(), end=' ')
        print()


if __name__ == "__main__":
    main()