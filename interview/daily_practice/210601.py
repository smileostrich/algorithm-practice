# 주어진 문자열을 int 형으로 변환한다
def strtoint(s):
    i = 0
    num = 0
    isNeg = False
    lens = len(s)
    if s[0] == '-':
        isNeg = True
        i = 1
    while i < lens:
        num *= 10
        num += ord(s[i]) - ord('0')
        i += 1
    if isNeg:
        num = -num
    return num

print(strtoint('-357'))


# 주어진 int형을 str로 변환한다
def inttostr(i):
    s = ''
    isNeg = False
    if i == 0:
        return 0
    elif i < 0:
        i = -i
        isNeg = True
    while i > 0:
        s += chr((i % 10)+ord('0'))
        i //= 10
    if isNeg:
        s += '-'
    return s[::-1]

print(inttostr(-357))

# 주어진 문자열 역순 출력
def reverse(s):
    return s[::-1]

print(reverse('abcde'))

def reverse2(s):
    result = ''
    for i in range(len(s)-1,-1,-1):
        result += s[i]
    return result

print(reverse2('abcde'))

# 최소공배수 최대공약수
def bae(n1, n2):
    if n1 < n2:
        max = n2
    else:
        max = n1
    for i in range(max, (n1*n2)+1):
        if i % n1 == 0 and i % n2 == 0:
            res = i
            break
    return res

print(bae(3,2))


def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")