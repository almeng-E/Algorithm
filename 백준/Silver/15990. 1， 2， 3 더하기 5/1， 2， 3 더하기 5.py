import sys
input = sys.stdin.readline

# dp[2][4] --> 4를 만드는 수 중 +2 로 끝나는 수의 개수
# 초기 값 설정
dp = [[],
      [0, 1, 0, 1],  # +1 로 끝나는 수의 개수
      [0, 0, 1, 1],  # +2 로 끝나는 수의 개수
      [0, 0, 0, 1]]  # +3 로 끝나는 수의 개수

for _ in range(int(input())):
    N = int(input())
    if len(dp[1])-1 < N:
        # dp 생성
        for i in range(len(dp[1]), N+1):
            dp[1].append((dp[2][i-1] + dp[3][i-1])% 1000000009)
            dp[2].append((dp[1][i-2] + dp[3][i-2])% 1000000009)
            dp[3].append((dp[1][i-3] + dp[2][i-3])% 1000000009)

    print((dp[1][N] + dp[2][N] + dp[3][N])%1000000009)