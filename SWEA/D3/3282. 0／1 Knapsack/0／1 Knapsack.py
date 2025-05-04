def choice(idx, curr_weight):
    if curr_weight > K:
        return -float('inf')

    if idx == N:
        return 0

    if DP[idx][curr_weight] != -1:
        return DP[idx][curr_weight]

    a = item[idx][1] + choice(idx+1, curr_weight + item[idx][0])
    b = choice(idx+1, curr_weight)

    DP[idx][curr_weight] = max(a, b)
    return DP[idx][curr_weight]

T = int(input())
for TC in range(1, T+1):
    N, K = map(int, input().split())
    item = []
    for _ in range(N):
        item.append(tuple(map(int, input().split())))

    DP = [[-1 for _ in range(K+1)] for _ in range(N)]

    max_v = choice(0, 0)

    print(f'#{TC} {max_v}')