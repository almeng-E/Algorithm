import sys
input = sys.stdin.readline
MOD = 1_000_000_007
N = int(input())
S = '_' + input().rstrip()

# W, WH, WHE
WHEEs = 0
dp = [[0 for _ in range(3)] for _ in range(N+1)]
for i in range(1, N+1):
    tg = 5
    if S[i] == 'W':
        tg = 0
        dp[i][0] = (dp[i-1][0] + 1) % MOD
    elif S[i] == 'H':
        tg = 1
        dp[i][1] = (dp[i-1][1] + dp[i-1][0]) % MOD

    elif S[i] == 'E':
        tg = 2
        WHEEs *= 2
        WHEEs += dp[i-1][2]
        WHEEs %= MOD
        dp[i][2] = (dp[i-1][2] + dp[i-1][1]) % MOD

    for j in range(3):
        if tg == j:
            continue
        dp[i][j] = dp[i-1][j]

print(WHEEs % MOD)