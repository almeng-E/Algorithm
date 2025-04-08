import sys
input = sys.stdin.readline
N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

DP = [0] * (K+1)

items.sort(key=lambda x: x[0])

for item, value in items:
    for kg in range(K, item-1, -1):
        # 넣는게 이득인지 판단
        if DP[kg] < DP[kg - item] + value:
            DP[kg] = DP[kg - item] + value

print(DP[K])