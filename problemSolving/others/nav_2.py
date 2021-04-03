def test(blocks):
    height = len(blocks)
    dic_blocks = {i+1:[False]*(i+1) for i in range(height)}

    for i in range(height):
        dic_blocks[i+1][blocks[i][0]] = blocks[i][1]
    for idx in range(1, height+1):
        if idx != height:
            visited = [False for _ in range(idx+1)]
            visited[blocks[idx][0]] = True
            next_val = [blocks[idx][0]]
            while next_val:
                cur = next_val.pop()
                if cur == idx and not visited[cur-1]:
                    dic_blocks[idx+1][cur-1] = dic_blocks[idx][cur-1] - dic_blocks[idx+1][cur]
                    next_val.append(cur-1)
                    visited[cur-1] = True
                elif cur == 0 and not visited[cur+1]:
                    dic_blocks[idx + 1][cur + 1] = dic_blocks[idx][0] - dic_blocks[idx + 1][cur]
                    next_val.append(cur + 1)
                    visited[cur + 1] = True
                else:
                    if cur-1 >= 0 and not visited[cur-1]:
                        dic_blocks[idx+1][cur-1] = dic_blocks[idx][cur-1] - dic_blocks[idx+1][cur]
                        next_val.append(cur - 1)
                        visited[cur - 1] = True
                    if cur+1 <= idx and not visited[cur+1]:
                        dic_blocks[idx + 1][cur + 1] = dic_blocks[idx][cur] - dic_blocks[idx + 1][cur]
                        next_val.append(cur + 1)
                        visited[cur + 1] = True
    final = []
    for k in dic_blocks.values():
        final.extend(k)
    return final


print(test([[0,50],[0,22],[2,10],[1,4],[4,-13]]))
print(test([[0,92],[1,20],[2,11],[1,-81],[3,98]]))