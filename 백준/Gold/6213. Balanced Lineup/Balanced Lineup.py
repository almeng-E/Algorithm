import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
LEN = 1
while LEN < N:
    LEN <<= 1

big = [0] * (LEN * 2)
small = [float('inf')] * (LEN * 2)

for i in range(N):
    a = int(input())
    big[i+LEN] = a
    small[i+LEN] = a

for i in range(LEN-1, 0, -1):
    big[i] = max(big[i*2], big[i*2+1])
    small[i] = min(small[i*2], small[i*2+1])

out = []
for _ in range(Q):
    a, b = map(int, input().split())
    l, r = a+LEN-1, b+LEN-1
    B, S = 0, float('inf')

    while l <= r:
        if l%2 == 1:
            B = max(B, big[l])
            S = min(S, small[l])
            l += 1
        if r%2 == 0:
            B = max(B, big[r])
            S = min(S, small[r])
            r -= 1
        l //= 2
        r //= 2

    out.append(str(B - S))

print('\n'.join(out))
