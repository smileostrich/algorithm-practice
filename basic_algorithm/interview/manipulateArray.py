arr = [[1,2,3],[4,5,6],[7,8,9]]


# return tuple
def arrMove(array):
    return list(zip(*reversed(array)))
    # return list(zip(*arr[::-1]))


# return list
# memory save
def roatated(array):
    test = list(zip(*reversed(array)))
    # test = list(zip(*array[::-1]))
    return [list(elem) for elem in test]

print(arrMove(arr))
print(roatated(arr))
