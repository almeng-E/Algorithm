import sys
input = sys.stdin.readline
N = int(input())
dp = [0, 0]
def find():
    for i in range(2, N+1):
        if i%3 == 0:
            if i%2 != 0:
                dp.append(min(dp[i//3], dp[i-1]) + 1)
            else:
                dp.append(min(dp[i//3], dp[i//2], dp[i-1]) + 1)
        elif i%2 == 0:
            dp.append(min(dp[i//2], dp[i-1]) + 1)
        else:
            dp.append(dp[i-1] + 1)

    print(dp[N])
find()