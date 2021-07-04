def organizingContainers(container):
    size_ball = len(container[0])
    container.sort(key=lambda x: -sum(x))
    for idx, balls in enumerate(container):
        if idx+1 < size_ball:
            for i in range(idx+1,size_ball):
                if container[i][idx] > 0:
                    container[i][idx], container[idx][idx], tmp = 0, container[idx][idx] + container[i][idx], container[i][idx]
                    c_idx = 0
                    while tmp > 0 and c_idx < size_ball:
                        if c_idx != idx and container[idx][c_idx] != 0:
                            if tmp > container[idx][c_idx]:
                                tmp -= container[idx][c_idx]
                                container[idx][c_idx], container[i][c_idx] = 0, container[i][c_idx]+container[idx][c_idx]
                            else:
                                container[idx][c_idx], container[i][c_idx] = container[idx][c_idx]-tmp, container[i][c_idx] + tmp
                                tmp = 0
                                break
                        c_idx += 1
                    else:
                        return 'Impossible'
    for c in range(len(container)):
        for i in range(len(container)):
            if i != c:
                if container[i][c]:
                    return 'Impossible'
    return 'Possible'



print(organizingContainers([[0, 2, 1],[1, 1, 1],[2, 0, 0]]))
print(organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]]))