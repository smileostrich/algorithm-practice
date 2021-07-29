def largestArea(samples):
    cnt = 0
    for sample in samples:
        cnt += sum(sample)
        if cnt > 0:
            break
    else:
        return 0

    for i in range(len(samples),1,-1):
        for y in range(len(samples)-i+1):
            for x in range(len(samples)-i+1):
                flag = False
                for in_y in range(i):
                    if not flag:
                        for in_x in range(i):
                            if not flag:
                                if samples[y+in_y][x+in_x] != 1:
                                    flag = True
                                    break
                            else:
                                break
                    else:
                        break
                if not flag:
                    return i
print(largestArea([[1, 1, 1], [1, 1, 0], [1, 0, 1]]))