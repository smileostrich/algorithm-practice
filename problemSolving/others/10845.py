# Queue 18분

import sys


N = int(sys.stdin.readline())
test = [sys.stdin.readline().rstrip() for _ in range(N)]


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return -1
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        if len(self.items) == 0:
            return 1
        return 0

    def front(self):
        if len(self.items) == 0:
            return -1
        return self.items[-1]

    def back(self):
        if len(self.items) == 0:
            return -1
        return self.items[0]


testqueue = Queue()

for i in test:
    if i == 'front':
        print(testqueue.front())
    elif i == 'back':
        print(testqueue.back())
    elif i == 'size':
        print(testqueue.size())
    elif i == 'empty':
        print(testqueue.empty())
    elif i == 'pop':
        print(testqueue.pop())
    else:
        push, num = i.split()
        testqueue.push(num)

