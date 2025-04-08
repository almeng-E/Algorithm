import sys
input = sys.stdin.readline
N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

bef_DP = [0] * (K+1)


for item, value in items:
    aft_DP = bef_DP[:]
    for kg in range(item, K+1):
        # 넣는게 이득인지 판단
        if aft_DP[kg] < bef_DP[kg - item] + value:
            aft_DP[kg] = bef_DP[kg - item] + value
    bef_DP = aft_DP
print(bef_DP[K])