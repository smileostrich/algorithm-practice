from sys import stdin

# 첫번째 방법

def comb_check(hand_n, hand_s):
    hand_n.sort(reverse=True)
    straight, flush = False, False
    set_hand_n = set(hand_n)
    len_hand_n = len(set_hand_n)

    if len(set(hand_s)) == 1:
        flush = True
    if len_hand_n == 5 and hand_n[0]-hand_n[4] == 4:
        straight = True
    if straight & flush:vdgiojjkllkj
        return 8, hand_n[0]
    elif flush:
        return 5, hand_n # 같을때 숫자 비교
    elif straight:
        return 4, hand_n[0]
    elif len_hand_n == 2:
        # 포카드
        if hand_n[0] == hand_n[3]:
            return 7, hand_n[0]
        elif hand_n[1] == hand_n[4]:
            return 7, hand_n[4]
        # 풀 하우스
        if hand_n[0] == hand_n[2]:
            return 6, [hand_n[0], hand_n[-1]]
        else:
            return 6, [hand_n[-1], hand_n[0]]
    elif len_hand_n == 3:
        for c in set_hand_n:
            # 쓰리
            if hand_n.count(c) == 3:
                return 3, c
            # 투페어
            else:
                tmp = [c]
                for k in set_hand_n:
                    if k == c:
                        continue
                    elif hand_n.count(k) == 2:
                            tmp.append(k)
                tmp.sort(reverse=True)
                return 2, tmp
    elif len_hand_n == 4:
        for c in set_hand_n:
            if hand_n.count(c) == 2:
                return 1, c
    else:
        return 0, hand_n # 같을때 숫자 비교


def check_win(my_comb, my_num, your_comb, your_num):
    if my_comb == your_comb:
        if my_comb in [0,2,5,6]:
            for my, your in zip(my_num, your_num):
                if my > your:
                    return 'WIN'
                elif my < your:
                    return 'LOSE'
            return 'DRAW'
        else:
        # if my_comb in [1,3,4,7,8]:
            if my_num > your_num:
                return 'WIN'
            elif my_num < your_num:
                return 'LOSE'
            else:
                return 'DRAW'
    elif my_comb > your_comb:
        return 'WIN'
    else:
        return 'LOSE'

my_hand = map(str, stdin.readline().split())
your_hand = map(str, stdin.readline().split())
my_hand_s = []
my_hand_n = []
your_hand_s = []
your_hand_n = []

# for card in map(str, 'S1 S2 H4 C3 H10'.split()):
# for card in map(str, 'S10 S1 D2 C3 H4'.split()):
for card in my_hand:
    my_hand_s.append(card[0])
    my_hand_n.append(int(card[1:]))
# for card in map(str, 'H3 D5 C8 C9 D2'.split()):
# for card in map(str, 'C2 C4 D4 H4 S7'.split()):
for card in your_hand:
    your_hand_s.append(card[0])
    your_hand_n.append(int(card[1:]))

my_comb, my_num = comb_check(my_hand_n, my_hand_s)
your_comb, your_num = comb_check(your_hand_n, your_hand_s)

print(check_win(my_comb, my_num, your_comb, your_num))
