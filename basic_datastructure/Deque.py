# 만약에 size 있으면 init에 만들어줘야함

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