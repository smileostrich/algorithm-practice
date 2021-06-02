a = [4,2,3,1,6]

def selection_sort(n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

def insertion_sort(n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


# selection_sort(len(a))
insertion_sort(len(a))
print(a)


n = 7
dp = [0 for _ in range(n+1)]
dp[1] = 1
dp[2] = 1
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp)

# 패턴 그리기
n = 10
for i in range(n,0,-1):
    for j in range(n,n-i,-1):
        print(j,end='')
    print('')

# 1000보다 작은 숫자 중 3과 5의 배수의 총합을 구하는 프로그램
n = 1000
t_sum = 0
for i in range(n):
    if i % 3 == 0 or i% 5 == 0:
        t_sum += i
print(t_sum)

# 10진수 8진수로
n = 11
binary = ''
while n > 0:
    div = n // 2
    mod = n % 2
    n = div
    binary += str(mod)
print(binary[::-1])

n = 11
binary = ''
while n > 0:
    binary = str(n%2) + binary
    n = n // 2
print(binary)

n = 100
binary = ''
while n > 0:
    binary = str(n%2) + binary
    n = n // 2

print(binary)


n = 100
binary = ''
while n > 0:
    binary = str(n%8) + binary
    n = n // 8
print(binary)

n = 1000
binary = ''
while n > 0:
    res = ''
    if n % 16 == 15:
        res = 'f'
    elif n% 16 == 14:
        res = 'e'
    elif n% 16 == 13:
        res = 'd'
    elif n% 16 == 12:
        res = 'c'
    elif n% 16 == 11:
        res = 'b'
    elif n% 16 == 10:
        res = 'a'
    else:
        res = str(n%16)
    binary = res + binary
    n = n // 16
print(binary)


def max_heapify(arr, n, idx):
    largest = idx
    l = 2 * idx + 1
    r = 2 * idx + 2

    if l < n and arr[idx] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # build heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # sorting
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)