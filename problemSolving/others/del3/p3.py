def countTeams(skills, minPlayers, minLevel, maxLevel):
    skills.sort()

    for idx, i in enumerate(skills):
        if i >= minLevel:
            min_idx = idx
            break
    for i in range(len(skills) - 1, -1, -1):
        if skills[i] <= maxLevel:
            max_idx = i
            break
    print(min_idx,max_idx)


print(countTeams([4, 8, 5, 6],1, 5, 7))