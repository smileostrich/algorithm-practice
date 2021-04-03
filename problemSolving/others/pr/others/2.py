def solution(enroll, referral, seller, amount):
    dic_member = {i:[] for i in enroll}
    dic_parent = {i:[] for i in enroll}
    dic_answer = {i:0 for i in enroll}
    dic_sell = {i:0 for i in enroll}
    for idx in range(len(referral)):
        if referral[idx] != '-':
            dic_member[referral[idx]].append(enroll[idx])
            dic_parent[enroll[idx]].append(referral[idx])
    for i in range(len(seller)):
        dic_sell[seller[i]] = amount[i]*100
    for sel, pri in dic_sell.items():
        cur_pri = pri
        dq = [sel]
        while dq:
            cur = dq.pop()
            dic_answer[cur] += int(0.9 * cur_pri)
            cur_pri = int(0.1 * cur_pri)
            if dic_parent[cur]:
                dq.append(dic_parent[cur])
    return dic_answer

["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	["young", "john", "tod", "emily", "mary"]	[12, 4, 2, 5, 10]	[360, 958, 108, 0, 450, 18, 180, 1080]
["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	["sam", "emily", "jaimie", "edward"]	[2, 3, 5, 4]	[0, 110, 378, 180, 270, 450, 0, 0]