# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.qhead = None
#
#     def isempty(self):
#         if self.head == None:
#             return True
#         else:
#             return False
#
#     def push(self, data):
#         if self.isempty():
#             self.head = Node(data)
#             self.qhead = self.head
#         else:
#             newnode = Node(data)
#             newnode.next = self.head
#             self.head = newnode.data
#
#     def pop(self):
#         if self.isempty():
#             print('stack underflow occured')
#         else:
#             tmp = self.head
#             self.head = tmp.next
#             print(tmp.data)
#
#     def peek(self):
#         if self.isempty():
#             print('stack is empty')
#         else:
#             print(self.head.data)
#
#     def qpeek(self):
#         if self.isempty():
#             print('queue is empty')
#         else:
#             print(self.qhead.data)
#
#
# stack = Stack()
# stack.push('처음')
# stack.peek()
# stack.qpeek()
# stack.pop()
# stack.peek()
# stack.qpeek()

def heapify(arr,idx,heapsize):
    largest = idx
    l = idx * 2 + 1
    r = idx * 2 + 2
    if l < heapsize and arr[l] > arr[largest]:
        largest = l
    if r < heapsize and arr[r] > arr[largest]:
        largest = r
    if idx != largest:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr,largest,heapsize)

def heapsort(arr):
    size = len(arr)
    for i in range(size//2-1, -1,-1):
        heapify(arr, i, size)
    for i in range(size-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr,0,i)

arr = [10,9,8,7,6,5,4,3,2,1]
heapsort(arr)
print(arr)