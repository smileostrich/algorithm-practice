# list



# linked list
# class Heap:
#     def __init__(self):
#         self.h = []
#         self.currsize = 0
#
#     def leftChild(self, i):
#         if 2 * i + 1 < self.currsize:
#             return 2 * i + 1
#         return None
#
#     def rightChild(self, i):
#         if 2 * i + 2 < self.currsize:
#             return 2 * i + 2
#         return None
#
#     def maxHeapify(self, node):
#         if node < self.currsize:
#             m = node
#             lc = self.leftChild(node)
#             rc = self.rightChild(node)
#             if lc is not None and self.h[lc] > self.h[m]:wdfvcf
#                 m = lc
#             if rc is not None and self.h[rc] > self.h[m]:
#                 m = rc
#             if m != node:
#                 temp = self.h[node]
#                 self.h[node] = self.h[m]
#                 self.h[m] = temp
#                 self.maxHeapify(m)
#
#     def buildHeap(self, a):
#         self.currsize = len(a)
#         self.h = list(a)
#         for i in range(self.currsize // 2, -1, -1):
#             self.maxHeapify(i)
#
#     def getMax(self):
#         if self.currsize >= 1:
#             me = self.h[0]
#             temp = self.h[0]
#             self.h[0] = self.h[self.currsize - 1]
#             self.h[self.currsize - 1] = temp
#             self.currsize -= 1
#             self.maxHeapify(0)
#             return me
#         return None
#
#     def heapSort(self):
#         size = self.currsize
#         while self.currsize - 1 >= 0:
#             temp = self.h[0]
#             self.h[0] = self.h[self.currsize - 1]
#             self.h[self.currsize - 1] = temp
#             self.currsize -= 1
#             self.maxHeapify(0)
#         self.currsize = size
#
#     def insert(self, data):
#         self.h.append(data)
#         curr = self.currsize
#         self.currsize += 1
#         while (curr - 1) // 2 >= 0 and self.h[curr] > self.h[(curr - 1) // 2]:
#             temp = self.h[(curr - 1) // 2]
#             self.h[(curr - 1) / 2] = self.h[curr]
#             self.h[curr] = temp
#             curr = (curr - 1) // 2
#
#     def display(self):
#         print(self.h)
