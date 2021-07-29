from collections import defaultdict

def programmerStrings(s):
    dic_cnt = defaultdict(list)
    for idx, i in enumerate(s):
        dic_cnt[i].append(idx)
    dic_revcnt = {i:len(dic_cnt[i]) for i in set(list('programmer'))}
    dic_prcnt = {i:0 for i in set(list('programmer'))}
    for i in list('programmer'):
        dic_prcnt[i] += 1
        dic_revcnt[i] -= 1

    fir_last = 0
    for k,v in dic_prcnt.items():
        if dic_cnt[k][v-1] > fir_last:
            fir_last = dic_cnt[k][v-1]
    sec_fir = len(s)

    for k,v in dic_revcnt.items():
        if dic_cnt[k][v] <= sec_fir:
            sec_fir = dic_cnt[k][v]
    return sec_fir - fir_last -1




print(programmerStrings('progxrammerrxproxgrammer'))