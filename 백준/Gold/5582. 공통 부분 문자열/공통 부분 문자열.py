import sys
input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()
ans = 0
dp = [[0 for _ in range(len(S1)+1)] for _ in range(len(S2)+1)]
for i in range(len(S2)):
    for j in range(len(S1)):
        if S1[j] == S2[i]:
            dp[i+1][j+1] = dp[i][j] + 1
            ans = max(ans, dp[i+1][j+1])

print(ans)