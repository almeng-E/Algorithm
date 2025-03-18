N = int(input())
arr = list(map(int, input().split()))

lis_dp = [1] * N
sum_dp = arr[:]

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            sum_dp[i] = max(sum_dp[i], sum_dp[j] + arr[i])

print(max(sum_dp))
