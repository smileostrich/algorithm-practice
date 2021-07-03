def solution(snowballs):
    idx = 0
    while idx < len(snowballs):
        snow = snowballs[idx]
        if snow > 0:
            i = idx + 1
            while i < len(snowballs):
                if snowballs[i] < 0:
                    if -snowballs[i] > snow:
                        snowballs.pop(idx)
                        if idx > 0:
                            idx -= 1
                        break
                    elif -snowballs[i] == snow:
                        snowballs.pop(i)
                        snowballs.pop(idx)
                        if idx > 0:
                            idx -= 1
                        break
                    else:
                        snowballs.pop(i)
                        # i += 1

                else:
                    idx += 1
                    break
            else:
                idx += 1
        else:
            i = idx-1
            while i != -1:
                if snowballs[i] > 0:
                    if snowballs[i] > -1*snow:
                        snowballs.pop(idx)
                        if idx > 0:
                            idx -= 1
                        break
                    elif snowballs[i] == -1*snow:
                        snowballs.pop(idx)
                        snowballs.pop(i)
                        if idx > 0:
                            idx -= 1
                        break
                    else:
                        snowballs.pop(i)
                        # i -= 1
                else:
                    idx += 1
                    break
            else:
                idx += 1
    return snowballs




print(solution(	[7,-6,12,-11]))