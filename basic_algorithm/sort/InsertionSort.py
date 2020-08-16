import unittest


def insertionSort(list):
    for idx, valueToInsert in enumerate(list):
        # select the hole position where number is to be inserted
        holePosition = idx

        # check if previous no. is larger than value to be inserted
        while holePosition > 0 and list[holePosition - 1] > valueToInsert:
            list[holePosition - 1], list[holePosition] = list[holePosition], list[holePosition - 1]
            holePosition = holePosition - 1
    return list


class SortTest(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], insertionSort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertionSort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertionSort([6, 5, 4, 3, 2, 1]))