N = int(input())

# 초기 상태 만들기 1-index
DP = [[0] for _ in range(10)]
DP[0].append(0)
for i in range(1, 10):
    DP[i].append(1)

MOD = 1000000000
# DP[번호값][층]

# i : 2층 ~ N층 계산
for i in range(2, N+1):
    # 번호값 == 0 인 경우
    DP[0].append(DP[1][i-1] % MOD)

    # 번호값 == 1 ~ 8 인 경우
    for v in range(1, 9):
        DP[v].append((DP[v-1][i-1] + DP[v+1][i-1]) % MOD)

    # 번호값 == 9 인 경우
    DP[9].append(DP[8][i-1] % MOD)

res = 0
for v in range(10):
    res += DP[v][N]
    res %= MOD
print(res)