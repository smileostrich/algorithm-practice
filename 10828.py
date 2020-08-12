# stack 문제 17분

import sys


N = int(sys.stdin.readline())
command = [sys.stdin.readline().rstrip() for _ in range(N)]

class Stack:
    def __init__(self):
        self.items = []
        self.max = 10000

    def push(self, item):
        if self.max != len(self.items):
            self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return -1
        elif len(self.items) != 0:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        if len(self.items) == 0:
            return 1
        elif not len(self.items) == 0:
            return 0

    def top(self):
        if len(self.items) != 0:
            return self.items[-1]
        elif len(self.items) == 0:
            return -1


tstack = Stack()
for i in command:
    if i == 'top':
        print(tstack.top())
    elif i == 'size':
        print(tstack.size())
    elif i == 'empty':
        print(tstack.empty())
    elif i == 'pop':
        print(tstack.pop())
    else:
        push, val = i.split()
        tstack.push(val)
