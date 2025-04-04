import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    DP = [0] * (M+1)    # 1-index
    DP[0] = 1

    for coin in coins:
        if coin > M:
            break
        for j in range(coin, M+1):
            DP[j] += DP[j-coin]
    print(DP[M])

