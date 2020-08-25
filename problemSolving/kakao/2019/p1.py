s = "aabbaabbd"

ls = len(s)
# for i in range(1, len(s)+1):
#     prefix = s[:i]
#     suffix = s[i:]
    # print(prefix)
    # print(suffix)
test(ls,2)
def test(ls, n):
    for i in range(ls//n,0,-1):
        li[0:] =
        # s[:i]
        # s[i:2*i]
        if s[:i] == s[i:2*i]:
            test(ls,i)