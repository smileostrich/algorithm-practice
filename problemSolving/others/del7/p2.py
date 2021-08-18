def solution(seconds):
    snack_dic = {'300': 10, '130': 30, '120': 20, '20': 30}
    snack_list = [300, 130, 120, 20]

    count = 0

    while seconds > 0:
        if seconds == 0:
            break
        for time in snack_list:
            if time <= seconds and snack_dic[str(time)] > 0:
                tmp = seconds - time
                if tmp < 120 and tmp % 20 != 0:
                    continue
                else:
                    seconds -= time
                    snack_dic[str(time)] -= 1
                    count += 1
                    break

    return count


print(solution(500))