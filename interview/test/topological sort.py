MAX_N = 25
MAX_M = 25
CONNECTED = 1
NOT_CONNECTED = 0
NOT_UPDATED_YET = 0
NOT_VISITED = -1
DUPLICATE = -2

Map = [[0] * MAX_N for i in range(MAX_N)]
count = [0] * MAX_N
queue = []
stack = []
nodes = []


def mark_duplicate(item):
    for i in range(0, len(stack)):
        if stack[i] == item:
            stack[i] = DUPLICATE


class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None

    def reset(self):
        self.prev = None

    def push(self, other):
        if self.prev == None:
            self.prev = other
            return
        head = self
        while head.prev != None:
            head = head.prev
        head.prev = other


for i in range(0, MAX_N):
    nodes.append(Node(i))


def reset():
    for i in range(0, MAX_N):
        for j in range(0, MAX_N):
            Map[i][j] = 0
    for i in range(0, MAX_N):
        count[i] = 0
    queue.clear()
    stack.clear()
    for i in range(0, MAX_N):
        nodes[i].reset()


def connected(src, dest):
    return Map[src][dest] == CONNECTED


def traverse(idx):
    mark_duplicate(nodes[idx].item)
    stack.append(nodes[idx].item)
    cur = nodes[idx].prev
    while cur != None:
        traverse(cur.item)
        cur = cur.prev


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        dest = int(input())
        reset()

        for i in range(0, m):
            s, d = map(int, input().split())
            Map[s - 1][d - 1] = CONNECTED
            count[d - 1] += 1

        for i in range(0, n):
            if count[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            src = queue.pop(0)
            for i in range(0, n):
                if connected(src, i):
                    node = Node(src)
                    nodes[i].push(node)
                    count[i] -= 1
                    if count[i] == 0:
                        queue.append(i)

        print("#%d " % test_case, end='')

        if nodes[dest - 1].prev == None:
            print("Not reached")
        else:
            traverse(dest - 1)
            while len(stack) > 0:
                item = stack.pop()
                if item == DUPLICATE:
                    continue
                print("%d " % (item + 1), end='')
            print()


if __name__ == "__main__":
    main()