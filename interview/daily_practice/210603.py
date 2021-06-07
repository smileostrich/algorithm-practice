def heapify(arr,i,heap_size):
    largest = i
    l = i * 2 + 1
    r = i * 2 + 2
    if l < heap_size and arr[l] > arr[largest]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if i != largest:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr,largest,heap_size)

def heapsort(arr):
    size = len(arr)
    for i in range(size//2-1, -1,-1):
        heapify(arr,i,size)
    for i in range(size-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,0,i)

arr = [1,2,3,4,5,6,7,8,9,10]
heapsort(arr)
print(arr)

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
        ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
    return a

def binsearch(arr,target,l,r):
    if l <= r:
        mid = l + (r-l)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binsearch(arr, target, mid+1, r)
        else:
            return binsearch(arr, target, l, mid-1)
    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9,10]
print(binsearch(arr,0, 0,len(arr)-1))


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        memo = [0,1,1]
        for i in range(3,n+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[-1]


print(fibo(8))
# 0 1 1 2 3 5 8 13 21

def factorial(n,res):
    if n == 0:
        return res
    else:
        return factorial(n-1,res*n)


print(factorial(5,1))
# 5 * 4 * 3 * 2 * 1 = 120
print(factorial(0,1))


import random

def radombool():
    t_li = []
    res = []
    for _ in range(10):
        cur = random.randint(1,10)
        if cur in t_li:
            res.append(True)
        else:
            res.append(False)
            t_li.append(cur)
    return res

print(radombool())

import unittest


class Stack:
    def __init__(self):
        self.items = []
        self.max = 5

    def push(self, item):
        if len(self.items) < self.max:
            self.items.append(item)
        else:
            print("error occured. abort push in order to prevent stack overflow")

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("error occured. stack is empty, abort pop to prevent stack underflow")

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class StackTest(unittest.TestCase):
    def test(self):
        st = Stack()
        self.assertTrue(st.is_empty())
        self.assertEqual(st.size(), 0)
        st.push(1)
        st.push(2)
        st.print_stack()
        st.pop()
        st.print_stack()
        st.push(3)
        self.assertEqual(st.peek(),3)
        self.assertFalse(st.is_empty())
        self.assertEqual(st.size(), 2)
        st.pop()
        st.pop()
        st.pop()
        st.push(3)
        st.push(3)
        st.push(3)
        st.push(3)
        st.push(3)
        st.push(3)
