def get_prefix_table(needle):
    prefix_set = set()
    n = len(needle)
    prefix_table = [0]*n
    delimeter = 1
    while(delimeter<n):
        prefix_set.add(needle[:delimeter])
        j = 1
        while(j<delimeter+1):
            if needle[j:delimeter+1] in prefix_set:
                prefix_table[delimeter] = delimeter - j + 1
                break
            j += 1
        delimeter += 1
    return prefix_table

def strstr(haystack, needle):
    # m: denoting the position within S where the prospective match for W begins
    # i: denoting the index of the currently considered character in W.
    haystack_len = len(haystack)
    needle_len = len(needle)
    if (needle_len > haystack_len) or (not haystack_len) or (not needle_len):
        return -1
    prefix_table = get_prefix_table(needle)
    m = i = 0
    while((i<needle_len) and (m<haystack_len)):
        if haystack[m] == needle[i]:
            i += 1
            m += 1
        else:
            if i != 0:
                i = prefix_table[i-1]
            else:
                m += 1
    if i==needle_len and haystack[m-1] == needle[i-1]:
        return m - needle_len
    else:
        return -1

if __name__ == '__main__':
    needle = 'abcaby'
    haystack = 'abxabcabcaby'
    print strstr(haystack, needle)


def kmp_matcher(t, d):
    n = len(t)
    m = len(d)

    pi = compute_prefix_function(d)
    q = 0
    i = 0
    while i < n:
        if d[q] == t[i]:
            q = q + 1
            i = i + 1
        else:
            if q != 0:
                q = pi[q - 1]
            else:
                i = i + 1
        if q == m:
            print
            "pattern occurs with shift " + str(i - q)
            q = pi[q - 1]


def compute_prefix_function(p):
    m = len(p)
    pi = range(m)
    k = 1
    l = 0
    while k < m:
        if p[k] <= p[l]:
            l = l + 1
            pi[k] = l
            k = k + 1
        else:
            if l != 0:
                l = pi[l - 1]
            else:
                pi[k] = 0
                k = k + 1
    return pi


def compute_prefix_function(p):
    m = len(p)
    pi = range(m)
    k = 1
    l = 0
    while k < m:
        if p[k] <= p[l]:
            l = l + 1
            pi[k] = l
            k = k + 1
        else:
            if l != 0:
                l = pi[l - 1]
            else:
                pi[k] = 0
                k = k + 1
    return pi