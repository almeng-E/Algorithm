import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
pre = [0] * (N+1)
for i in range(1, N+1):
    pre[i] = pre[i-1] ^ arr[i]
ans = 0
for _ in range(Q):
    s, e = map(int, input().split())
    ans ^= pre[e] ^ pre[s-1]
print(ans)