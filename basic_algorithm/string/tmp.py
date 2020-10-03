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