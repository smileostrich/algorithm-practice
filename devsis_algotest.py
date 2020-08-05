
# class Queue:
#
#     def __init__(self):
#         self.items = []
#
#     def enqueue(self, item):
#         self.items.insert(0, item)
#
#     def dequeue(self):
#         self.items.pop()
#
#     def print_queue(self):
#         print(self.items)
#
#     def is_empty(self):
#         return self.items == []
#
#     def size(self):
#         return len(self.items)
#

s1 = [4,99,2,6,7,13,88,76]
s2 = [6,88,13,4,99,2,7]
result = []
s1.sort()
s2.sort()

# queue = Queue()
for i in s2:
    for j in s1:
        if i == j:
            s1.remove(j)
            break

print(s1)

