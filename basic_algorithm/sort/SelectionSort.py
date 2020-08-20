import unittest

def selectionSort(list):
    for i in range(len(list) - 1):
        # assume the min is the first element
        idx_min = i
        j = i + 1

        # test against elements after i to find the smallest
        while j < len(list):
            if(list[j] < list[idx_min]):
                # found new minimum; remember its index
                idx_min = j
            j = j + 1

        if idx_min is not i:
            # swap
            list[idx_min], list[i] = list[i], list[idx_min]

    return list

class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], selectionSort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selectionSort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selectionSort([6, 5, 4, 3, 2, 1]))