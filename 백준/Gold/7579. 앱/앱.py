N, M = map(int, input().split())

ms = list(map(int, input().split()))
cs = list(map(int, input().split()))

arr = list(zip(ms, cs))

target = sum(ms)-M
DP = [sum(cs)] * (target+1)

for byte, cost in arr:
    for i in range(0, target+1-byte):
        DP[i] = min(DP[i], DP[i+byte] - cost)
print(DP[0])