MOD = 1000000000
N, K = map(int, input().split())

# 초기 상황 설정
# 1-index
# DP[개수][합] ... 개수 : 1 ~ K | 합 : 0 ~ N
DP = [[1 for _ in range(N+1)] for _ in range(K+1)]

for i in range(2, K+1):
    for j in range(1, N+1):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1]) % MOD

print(DP[K][N])