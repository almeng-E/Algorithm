import sys
input = sys.stdin.readline

N = int(input())
rooms = list(map(int, input().split()))

# 0 번 사용 X
DP = [[0 for _ in range(N)] for _ in range(2)]
DP[0][0] += rooms[0]
for i in range(1, N):
    DP[0][i] = max(DP[0][i-1], DP[1][i-1]) + rooms[i]
    DP[1][i] = DP[0][i-1] + 1
res = max(DP[0][N-1], DP[1][N-1])


# 0 번 사용 O
DP = [[0 for _ in range(N)] for _ in range(2)]
DP[1][0] = 1
for i in range(1, N):
    DP[0][i] = max(DP[0][i-1], DP[1][i-1]) + rooms[i]
    DP[1][i] = DP[0][i-1] + 1
DP[1][N-1] = 0
res = max(DP[0][N-1], DP[1][N-1], res)
print(res)
