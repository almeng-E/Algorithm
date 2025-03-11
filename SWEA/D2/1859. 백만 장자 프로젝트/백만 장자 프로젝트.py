T = int(input())
for TC in range(T):
    N = int(input())

    prices = list(map(int, input().split()))

    mp = [0] * (N+1)
    for i in range(N-1, -1, -1):
        if prices[i] > mp[i+1]:
            mp[i] = prices[i]
        else:
            mp[i] = mp[i+1]
    res = 0

    for i in range(N):
        if mp[i] > prices[i]:
            res += mp[i] - prices[i]
    print(f'#{TC+1} {res}')