N = int(input())
cur = 666
cnt = 0

while True:
    if '666' in str(cur):
        cnt += 1
    if cnt == N:
        print(cur)
        break
    cur += 1