from sys import stdin
import collections

test_case = int(stdin.readline())


def idx_check(N, idx):
    if idx-1 < 0:
        return 0
    else:
        return idx-1

def target_check(N, target):
    if target-1 < 0:
        return N-1
    else:
        return target - 1


for _ in range(test_case):
    N, target = map(int, stdin.readline().split())
    if N == 1:
        stdin.readline()
        print(1)
    else:
        imp_list = collections.deque(map(int, stdin.readline().split()))
        arranged_list = sorted(imp_list)
        # biggest = arranged_list.pop()
        # test = {i:0 for i in range(N)}

        cnt_print = 0
        idx = 0
        biggest_idx = N-1

        while imp_list:
            # if idx == target:
            if 0 == target:
                if imp_list[0] < arranged_list[biggest_idx]:
                    imp_list.append(imp_list.popleft())
                    # idx = idx_check(len(imp_list),idx)
                    target = target_check(len(imp_list), target)

                else:
                    print(cnt_print+1)
                    break
            else:
                if imp_list[0] < arranged_list[biggest_idx]:
                    imp_list.append(imp_list.popleft())
                    # idx = idx_check(len(imp_list),idx)
                    target = target_check(len(imp_list), target)
                else:
                    cnt_print += 1
                    imp_list.popleft()
                    # idx = idx_check(len(imp_list),idx)
                    target = target_check(len(imp_list), target)
                    biggest_idx -= 1
