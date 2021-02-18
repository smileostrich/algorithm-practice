T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    size_s1 = len(str1)
    size_s2 = len(str2)
    cond = False
    for i in range((size_s2 - size_s1)+1):
        if cond == True:
            break
        for j in range(size_s1):
            if str1[j] != str2[i+j]:
                break
        else:
            cond = True
    if cond == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')