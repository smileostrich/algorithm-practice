# 덱 14분

import sys


N = int(sys.stdin.readline())
commands = [sys.stdin.readline().rstrip() for _ in range(N)]


class Deque:
    def __init__(self):
        self.items = []

    def pushFront(self, item):
        self.items.insert(0, item)

    def pushBack(self, item):
        self.items.append(item)

    def popFront(self):
        if len(self.items) == 0:
            return -1
        return self.items.pop(0)

    def popBack(self):
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
        return self.items[0]

    def back(self):
        if len(self.items) == 0:
            return -1
        return self.items[-1]


testDeque = Deque()

for i in commands:
    if i == 'front':
        print(testDeque.front())
    elif i == 'back':
        print(testDeque.back())
    elif i == 'size':
        print(testDeque.size())
    elif i == 'empty':
        print(testDeque.empty())
    elif i == 'pop_front':
        print(testDeque.popFront())
    elif i == 'pop_back':
        print(testDeque.popBack())
    else:
        cm, num = i.split()
        if cm == 'push_back':
            testDeque.pushBack(num)
        elif cm == 'push_front':
            testDeque.pushFront(num)