import sys
input = sys.stdin.readline


def ADD(idx):
    global MAX_FREQ
    v = arr[idx]
    freq[cnt[v]] -= 1
    cnt[v] += 1
    freq[cnt[v]] += 1
    if MAX_FREQ < cnt[v]:
        MAX_FREQ = cnt[v]


def REMOVE(idx):
    global MAX_FREQ
    v = arr[idx]
    freq[cnt[v]] -= 1
    if MAX_FREQ == cnt[v] and freq[cnt[v]] == 0:
        MAX_FREQ -= 1
    cnt[v] -= 1
    freq[cnt[v]] += 1


N = int(input())
arr = [0] + list(map(int, input().split()))

M = int(input())
Q = []
for idx in range(M):
    l, r = map(int, input().split())
    Q.append((l, r, idx))
sqrtN = int(N**0.5)
Q.sort(key=lambda x: (x[0]//sqrtN, x[1]))

ans = [0] * M

cnt = [0] * 100_001     # cnt[값] : 등장 횟수
freq = [0] * 100_001    # freq[등장횟수] : cnt[v]가 몇개인지 체크
MAX_FREQ = 0

l, r = 1, 0


for ql, qr, idx in Q:
    while ql < l:
        l -= 1
        ADD(l)

    while ql > l:
        REMOVE(l)
        l += 1

    while r < qr:
        r += 1
        ADD(r)

    while r > qr:
        REMOVE(r)
        r -= 1

    ans[idx] = MAX_FREQ
print('\n'.join(map(str, ans)))

