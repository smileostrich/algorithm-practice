# next_permutation 호출할때마다 한번씩 수정
# e.g. 1,2,3 -> 1,3,2
def next_permutation(a):
    print(len(a)-1)
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break
    else:
        return False
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

a = [1,2,3,4,5,6,7]
for i in range(10):
    next_permutation(a)
print(a)