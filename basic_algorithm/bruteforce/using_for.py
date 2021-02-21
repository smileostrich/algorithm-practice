p = 'A pattern matching algorithm'
t = 'rithm'

def bruteForce(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break
        if cnt == M:
            return i
    return -1


print(bruteForce(p,t))