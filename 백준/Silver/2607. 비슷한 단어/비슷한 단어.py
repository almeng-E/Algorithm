import sys
input = sys.stdin.readline

N = int(input())
word = input().rstrip()
cnt = dict()
for c in word:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1

res = 0
for _ in range(N-1):
    s = input().rstrip()

    if abs(len(s) - len(word)) > 1:
        continue
    tmp = cnt.copy()
    for c in s:
        if c in tmp:
            tmp[c] -= 1
        else:
            tmp[c] = -1
    check = 0
    for v in tmp.values():
        if abs(v) > 1:
            break
        else:
            check += abs(v)
    else:
        if len(s) == len(word):
            if check <= 2:
                res += 1
        else:
            if check == 1:
                res += 1
print(res)
