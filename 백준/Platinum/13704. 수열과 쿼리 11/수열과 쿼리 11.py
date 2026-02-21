import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
M = int(input())
Q = []
for i in range(M):
    ql, qr = map(int,input().split())
    Q.append((ql-1, qr, i))
sqrtN = int(N ** 0.5)
Q.sort(key=lambda x: (x[0] // sqrtN, x[1] if (x[0] // sqrtN) % 2 == 0 else -x[1]))

MAX = 1
while MAX < 1_000_001:
    MAX <<= 1

ans = [0] * M
cnt = [0] * (MAX+1)
l, r = 1, 0
cur = 0

p_xor = [0] * (N + 1)
for i in range(1, N+1):
    p_xor[i] = arr[i] ^ p_xor[i - 1]


for ql, qr, qi in Q:
    while ql < l:
        l -= 1
        cur += cnt[p_xor[l] ^ K]
        cnt[p_xor[l]] += 1

    while l < ql:
        cnt[p_xor[l]] -= 1
        cur -= cnt[p_xor[l] ^ K]
        l += 1

    while r < qr:
        r += 1
        cur += cnt[p_xor[r] ^ K]
        cnt[p_xor[r]] += 1

    while qr < r:
        cnt[p_xor[r]] -= 1
        cur -= cnt[p_xor[r] ^ K]
        r -= 1

    ans[qi] = cur
print('\n'.join(map(str, ans)))
