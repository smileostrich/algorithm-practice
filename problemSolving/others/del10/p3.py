from datetime import datetime
import math
from collections import defaultdict

def solution(fees, records):
    b_time, b_fee, u_time, u_fee = fees

    dic_sig = defaultdict(list)
    time_format_str = '%d/%m/%Y %H:%M'

    li_result = []

    for i in records:
        cur_time, car, sig = i.split()
        dic_sig[car].append(datetime.strptime('1/8/2021 ' + cur_time, time_format_str))

    for k,v in dic_sig.items():
        if len(v) % 2 == 1:
            dic_sig[k].append(datetime.strptime('1/8/2021 23:59', time_format_str))
        tmp_s = dic_sig[k][1] - dic_sig[k][0]
        for i in range(2, len(dic_sig[k]), 2):
            diff = dic_sig[k][i+1] - dic_sig[k][i]
            tmp_s += diff
        t_result = int(math.ceil(tmp_s.total_seconds())/60)
        if t_result <= b_time:
            li_result.append((k, b_fee))
        else:
            li_result.append((k, b_fee + int(math.ceil((t_result - b_time) / u_time)) * u_fee))
    li_result.sort(key=lambda x:(x[0]))
    return list(map(list, zip(*li_result)))[1]


print(solution(	[180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))