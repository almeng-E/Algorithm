import sys
input = sys.stdin.readline

cow = {}
S = input().rstrip()
for i in range(26):
    cow[S[i]] = i

SS = input().rstrip()
cur = -1
cnt = 1
for c in SS:
    if cur < cow[c]:
        cur = cow[c]
    else:
        cur = cow[c]
        cnt += 1
print(cnt)
