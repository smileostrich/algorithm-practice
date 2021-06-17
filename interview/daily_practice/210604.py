def heapify(arr,idx,heap_size):
    largest = idx
    l = idx * 2 + 1
    r = idx * 2 + 2

    if l < heap_size and arr[l] > arr[largest]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(arr,largest,heap_size)

def heapsort(arr):
    size = len(arr)
    for i in range(size//2-1, -1, -1):
        heapify(arr,i,size)
    for i in range(size-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,0,i)


# arr = [1,2,3,4,5,6,7,8,9,10]
arr = [10,9,8,7,6,5,4,3,2,1]
heapsort(arr)
print(arr)
#
# class Queue:
#     def __init__(self):
#         self.size = 5
#         self.items = []
#
#     def enqueue(self, item):
#         if len(self.items) == 5:
#             print('queue overflow occured')
#         else:
#             self.items.insert(0, item)
#
#     def deque(self):
#         if len(self.items) > 0:
#             return self.items.pop()
#         else:
#             print('queue underflow occured')
#
#     def printqueue(self):
#         print(self.items)
#
#     def is_empty(self):
#         return self.items == []
#
#     def size(self):
#         return len(self.items)
#
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(4)
# queue.enqueue(3)
# queue.printqueue()
# print(queue.deque())
# queue.printqueue()


# class Stack:
#     def __init__(self):
#         self.max = 5
#         self.items = []
#         self.items2 = []
#
#     def push(self, item):
#         if len(self.items) != 5:
#             self.items.append(item)
#             self.enqueue(item)
#         else:
#             print("stack overflow occured")
#
#     def pop(self):
#         if len(self.items) > 0:
#             print("stack", self.items.pop())
#             self.dequeue()
#         else:
#             print("stack underflow occured")
#
#     def printall(self):
#         print(self.items, self.items2)
#
#     def enqueue(self, item):
#         self.items2.append(item)
#
#     def dequeue(self):
#         print('queue', self.items2.pop(0))
#
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(5)
# stack.push(4)
# stack.printall()
# stack.pop()
# stack.printall()

