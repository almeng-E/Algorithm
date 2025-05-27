from collections import deque

A, K = map(int, input().split())

dp = [float('inf')] * 1000001
dp[A] = 0
queue = deque()
queue.append(A)

while queue:
    x = queue.popleft()

    nx = x+1
    if nx <= K and dp[nx] > dp[x]+1:
        dp[nx] = dp[x] + 1
        queue.append(nx)
    nx = 2*x
    if nx <= K and dp[nx] > dp[x]+1:
        dp[nx] = dp[x] + 1
        queue.append(nx)

print(dp[K])