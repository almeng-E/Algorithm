N = int(input())
arr = [int(input()) for _ in range(N)]


DP = [[0 for _ in range(N)] for _ in range(3)]
DP[1][0] = arr[0]

for i in range(1, N):
    DP[0][i] = max(DP[0][i-1], DP[1][i-1], DP[2][i-1])
    DP[1][i] = DP[0][i-1] + arr[i]
    DP[2][i] = DP[1][i-1] + arr[i]

print(max(DP[0][N-1], DP[1][N-1], DP[2][N-1]))