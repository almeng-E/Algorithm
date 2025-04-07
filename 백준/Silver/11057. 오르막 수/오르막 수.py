MOD = 10007
N = int(input())
DP = [[0 for _ in range(10)] for _ in range(N)]
for i in range(10):
    DP[0][i] = 1
for i in range(1, N):
    for j in range(10):
        DP[i][j] = sum(DP[i-1][:j+1]) % MOD
print(sum(DP[N-1])%MOD)