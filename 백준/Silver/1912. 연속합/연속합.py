import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

dp = [arr[0]]
res = 0
for i in range(1, N):
    if dp[i-1] > 0:
        dp.append(dp[i-1] + arr[i])
    else:
        dp.append(arr[i])
print(max(dp))