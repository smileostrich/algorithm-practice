class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.isempty():
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            tmp = self.head
            self.head = self.head.next
            return tmp.data

    def display(self):
        if self.isempty():
            print('Nothing')
        else:
            cur = self.head
            print(f'{cur.data} > ', end='')
            while cur.next:
                cur = cur.next
                print(f'{cur.data} > ', end='')
            print('')

MyStack = Stack()
MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

# Display stack elements
MyStack.display()
# Delete top elements of stack
MyStack.pop()
MyStack.pop()

# Display stack elements
MyStack.display()


def heapify(arr,heap_size,idx):
    largest = idx
    l = idx * 2 +1
    r = idx * 2 + 2
    if l < heap_size and arr[l] > arr[largest]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if idx != largest:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr,heap_size,largest)

def heapsort(arr):
    size = len(arr)
    for i in range(size//2-1, -1,-1):
        heapify(arr,size,i)
    print(arr)
    for i in range(size-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr,i,0)


arr = [10,9,8,7,6,5,4,3,2,1]
heapsort(arr)
print(arr)


def binsearch(arr, target,l,r):
    if l<=r:
        mid = l + (r-l)//2
        if arr[mid] < target:
            return binsearch(arr, target, mid + 1, r)
        elif arr[mid] > target:
            return binsearch(arr, target, l, mid - 1)
        else:
            return mid
    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9,10]
print(binsearch(arr,3, 0,len(arr)-1))


# def binsearch(arr, target, l, r):
#     if l <= r:
#         mid = l + (r - l) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return binsearch(arr, target, mid + 1, r)
#         else:
#             return binsearch(arr, target, l, mid - 1)
#     else:
#         return -1

def findfrequency(arr):
    dic_cnt = {}
    for i in arr:
        if i not in dic_cnt:
            dic_cnt[i] = 1
        else:
            dic_cnt[i] += 1
    print(sorted(dic_cnt.items(),key=lambda x: (-x[1],x[0])))

arr = ['a','a','c','b','a']
findfrequency(arr)


def fibo(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    result = [0,1,1]
    for i in range(3,n+1):
        result.append(result[i-1]+ result[i-2])
    return result

print(fibo(8))

