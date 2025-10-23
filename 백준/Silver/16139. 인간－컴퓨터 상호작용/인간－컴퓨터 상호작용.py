import sys
input = sys.stdin.readline

S = input().rstrip()

memo = [[(-1, 0)] for _ in range(26)]   # idx, cnt

for i in range(len(S)):
    j = ord(S[i]) - 97
    memo[j].append((i, memo[j][-1][1] + 1))

Q = int(input())
for _ in range(Q):
    cmd = input().split()
    l, r = int(cmd[1]), int(cmd[2])

    j = ord(cmd[0]) - 97
    lc, rc = 0, 0
    for idx, cnt in memo[j]:
        if idx < l:
            lc = max(lc, cnt)
        if idx <= r:
            rc = max(rc, cnt)

    print(rc-lc)