li_company = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
li_appli = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
li_result = ["A_bf", "B_ce", "C_d"]

dict_company = {}
dict_appli = {}
dict_result = {}

for i in li_company:
    a, b, c = i.split(' ')
    dict_company[a] = []
    for j in b:
        dict_company[a].append(j)
for i in li_appli:
    a, b, c = i.split(' ')
    dict_appli[a] = []
    for j in b:
        dict_appli[a].append(j)
for i in li_result:
    a, b = i.split('_')
    dict_result[a] = []
    for j in b:
        dict_result[a].append(j)
print(dict_company)
# print(dict_appli)
# print(dict_result)

