# 49분
def chk(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
            if cnt > 1:
                return 0
    else:
        return 1


def bfs(s, target, li_word):
    level = {s:0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for cur in frontier:
            for neighbor in li_word:
                if chk(neighbor, cur):
                    if neighbor == target:
                        return level[cur]+1
                    if neighbor not in level:
                        next.append(neighbor)
                        level[neighbor] = i
        frontier = next
        i += 1
    return 0


def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))