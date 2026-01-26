import sys
input = sys.stdin.readline
from bisect import bisect_left

N, Q = map(int, input().split())
P = [0] + list(map(int, input().split()))

P.sort()
SUM = [0] * (N+1)
SUM[0] = P[0]
for i in range(1, N+1):
    SUM[i] = SUM[i-1] + P[i]
ans = [0] * Q
for i in range(Q):
    x = int(input())
    lb = bisect_left(P, x)
    ans[i] = SUM[N] - 2 * SUM[lb-1] + x * (lb-1) - x * (N+1 - lb)
print('\n'.join(map(str, ans)))