from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort()

DP = [0] * (K+1)
DP[0] = 1

for coin in coins:
    for j in range(coin, K+1):
        DP[j] += DP[j-coin]
print(DP[K])