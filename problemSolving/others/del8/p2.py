class MovingTotal:
    def __init__(self):
        self.li_numbers = []
        self.dic_contains = dict()
        self.pointer = -1

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        for i in numbers:
            tmp = 0
            self.li_numbers.append(i)
            self.pointer += 1
            if self.pointer >= 2:
                for i in range(self.pointer, self.pointer - 3, -1):
                    tmp += self.li_numbers[i]
                self.dic_contains[tmp] = True
        pass

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        if total in self.dic_contains:
            return True
        else:
            return False


if __name__ == "__main__":
    movingtotal = MovingTotal()
    movingtotal2 = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    print('여기',movingtotal2.contains(6))
    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))