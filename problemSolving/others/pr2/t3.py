class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def selectNode(self, idx):
        if idx > self.size:
            return None
        if idx == 0:
            return self.head
        if idx == self.size:
            return self.tail
        if idx <= self.size // 2:
            target = self.head
            for _ in range(idx):
                target = target.next
            return target
        else:
            target = self.tail
            for _ in range(self.size - idx):
                target = target.prev
            return target

    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(value, None, self.head)
            tmp.prev = self.head
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.tail.prev
            newNode = Node(value, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1

    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendleft(value)
            elif tmp == self.tail:
                self.append(value)
            else:
                tmp_prev = tmp.prev
                newNode = Node(value, tmp_prev, tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
        self.size += 1

    def delete(self, idx):
        if self.is_empty():
            return
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
            elif tmp == self.tail:
                tmp = self.tail
                self.tail = self.tail.prev
            else:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            del (tmp)
            self.size -= 1

    def printlist(self):
        target = self.head
        re = []
        while target != self.tail:
            if target.next != self.tail:
                re.append(target.data)
            else:
                re.append(target.data)
            target = target.next
        return re

def solution(size, k, cmd):
    link = LinkedList()
    del_dq = []
    for i in range(size):
        link.append(i)
    idx = k
    for c in cmd:
        if c[0] == 'D':
            op,n = c.split()
            idx += int(n)
        elif c[0] == 'U':
            op, n = c.split()
            idx -= int(n)
        elif c[0] == 'C':
            del_dq.append((idx,link.selectNode(idx).data))
            link.delete(idx)
            if link.listSize()-1 <= idx:
                idx -= 1
        elif c[0] == 'Z':
            t_i, n = del_dq.pop()
            # if link.listSize()-1 < t_i:
            #     link.append(n)
            # else:
            for ei,i in enumerate(link.printlist()):
                if i > n:
                    link.insert(n,ei)
                    idx += 1
                    break
            else:
                link.append(n)
    result = ['X']*(size)
    for i in link.printlist():
        result[i] = 'O'
    return ''.join(result)

print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C", "C"]))