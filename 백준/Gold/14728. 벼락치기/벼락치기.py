N, T = map(int, input().split())

# 공부 시간 K , 배점 S
arr = [list(map(int, input().split())) for _ in range(N)]

DP = [0] * (T+1) # 1-index

for time, points in arr:
    for idx in range(T, time-1, -1):
        DP[idx] = max(DP[idx], DP[idx-time] + points)
print(DP[T])