s = input()
t = input()
# s = 'ab'
# t = 'abab'

size_s = len(s)
size_t = len(t)
if s * size_t == t * size_s:
    print(1)
else:
    print(0)
