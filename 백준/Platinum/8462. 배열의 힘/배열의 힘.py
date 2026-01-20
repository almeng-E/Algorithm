import sys
input = sys.stdin.readline

N, T = map(int, input().split())
arr = [0] + list(map(int, input().split()))
Q = []
for idx in range(T):
    a, b = map(int, input().split())
    Q.append((a, b, idx))
sqrtN = int(N**0.5)
Q.sort(key=lambda x: (x[0]//sqrtN, x[1]))
ans = [0] * T
cnt = [0] * 1_000_001
P = 0
l, r = 1, 0

for ql, qr, idx in Q:
    while ql < l:
        l -= 1
        v = arr[l]
        P -= v * cnt[v] * cnt[v]
        cnt[v] += 1
        P += v * cnt[v] * cnt[v]

    while l < ql:
        v = arr[l]
        P -= v * cnt[v] * cnt[v]
        cnt[v] -= 1
        P += v * cnt[v] * cnt[v]
        l += 1

    while r < qr:
        r += 1
        v = arr[r]
        P -= v * cnt[v] * cnt[v]
        cnt[v] += 1
        P += v * cnt[v] * cnt[v]

    while qr < r:
        v = arr[r]
        P -= v * cnt[v] * cnt[v]
        cnt[v] -= 1
        P += v * cnt[v] * cnt[v]
        r -= 1

    ans[idx] = P
print('\n'.join(map(str, ans)))