import unittest


def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)


list = [8, 13, 2, 6, 1, 4]
quicksort(list)
        # list = [8, 1, 2, 5, 10, 14, 7, 21]
        # self.assertEqual([1, 2, 5, 7, 8, 10, 14, 21], quicksort(list)