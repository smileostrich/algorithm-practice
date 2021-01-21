from sys import stdin

inp = lambda : stdin.readline().rstrip()

m = int(inp())
my_hand = list(map(int, inp().split()))
n = int(inp())
re_hand = list(map(int, inp().split()))
# m = 5
# my_hand = [6, 3, 2, 10, -10]
# n = 8
# re_hand = [10, 9, -5, 2, 3, 4, 5, -10]
my_hand.sort()
size = len(my_hand)

def bin_search(num):
    l = 0
    r = size - 1
    while l <= r:
        mid = (l+r) // 2
        if my_hand[mid] == num:
            return 1
        elif my_hand[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return 0

if __name__ == "__main__":
    result = []
    for num in re_hand:
        result.append(bin_search(num))
    print(*result)