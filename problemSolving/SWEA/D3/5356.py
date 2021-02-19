T = int(input())
for tc in range(1, T+1):
    li_word = []
    result = ''
    for _ in range(5):
        li_word.append(list(input()))
    maxi = 0
    for i in li_word:
        if len(i) > maxi:
            maxi = len(i)
    for j in li_word:
        while len(j) < maxi:
            j.append('')
    for k in range(maxi):
        for p in range(5):
            result += li_word[p][k]
    print(f'#{tc} {result}')
