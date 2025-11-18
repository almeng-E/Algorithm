import sys
input = sys.stdin.readline
def main():
    N, M, Q = map(int, input().split())
    
    lake = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(M):
        dp[0][j] = lake[0][j]
    for j in range(M):
        for i in range(1, N):
            lake[i][j] += lake[i-1][j]
            dp[i][j] = lake[i][j]
            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] += dp[i-1][j-1]
    
    res = []
    for _ in range(Q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        res.append(str(dp[a][b]))
    print('\n'.join(res))
main()