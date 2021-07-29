def insertion_sort(li):
    for i in range(1, len(li)):
        key = li[i]
        j = i - 1
        while j >= 0 and li[j] > key:
            li[j + 1] = li[j]
            j -= 1
        li[j+1] = key
    return li




class Stack:
    def __init__(self):
        self.size = 5
        self.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

class BinarySearchTree(object):
    def find(self, key):
        return self.