import sys

input = sys.stdin.readline

N = int(input())
# ( Ti , Pi )
li = [0] + [tuple(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(21)]

for i in range(N, 0, -1):
    if i + li[i][0] > N+1:
        dp[i] = max(dp[i+1:N+2])
    else:
        dp[i] = max(li[i][1] + dp[i+li[i][0]], *dp[i+1:N+2])
print(max(dp))