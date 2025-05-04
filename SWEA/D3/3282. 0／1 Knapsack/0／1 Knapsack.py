T = int(input())
for TC in range(1, T+1):
    N, K = map(int, input().split())
    item = []
    for _ in range(N):
        item.append(tuple(map(int, input().split())))

    DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(N-1, -1, -1):
        w, v = item[i]
        for j in range(K, -1, -1):
            take = v + (DP[i+1][j-w] if j>=w else -float('inf'))
            skip = DP[i+1][j]
            DP[i][j] = max(take, skip)

    print(f'#{TC} {DP[0][K]}')