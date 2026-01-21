import sys
input = sys.stdin.readline

def add(idx):
    global max_cnt
    C = color[idx]
    cnt_cnt[C_cnt[C]] -= 1
    C_cnt[C] += 1
    cnt_cnt[C_cnt[C]] += 1
    if max_cnt < C_cnt[C]:
        max_cnt = C_cnt[C]


def remove(idx):
    global max_cnt

    C = color[idx]
    cc = C_cnt[C]
    C_cnt[C] -= 1
    cnt_cnt[cc] -= 1
    if max_cnt == cc and cnt_cnt[cc] == 0:
        max_cnt -= 1
    cnt_cnt[C_cnt[C]] += 1



N, M = map(int, input().split())
color = [0] + list(map(int, input().split()))
Q = []
for i in range(M):
    X, Y = map(int, input().split())
    Q.append((X, Y, i))

sqrtN = int(N**0.5)
Q.sort(key=lambda x: (x[0]//sqrtN, x[1]))


ans = [0] * M
C_cnt = [0] * 200_002
cnt_cnt = [0] * 100_001
max_cnt = 0

l, r = 1, 0
for ql, qr, idx in Q:
    while l < ql:
        remove(l)
        l += 1

    while ql < l:
        l -= 1
        add(l)

    while r < qr:
        r += 1
        add(r)

    while qr < r:
        remove(r)
        r -= 1

    ans[idx] = max_cnt

print('\n'.join(map(str, ans)))