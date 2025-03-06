dp = [0, 1, 2, 4]
for i in range(4, 12):
    dp.append(sum(dp[i-3:i]))
for _ in range(int(input())):
    print(dp[int(input())])