T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ps = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + arr[i-1][j-1]

    ans = 0
    for r in range(0, N-M+1):
        for c in range(0, N-M+1):
            r2 = r + M
            c2 = c + M

            total = ps[r2][c2] - ps[r][c2] - ps[r2][c] + ps[r][c]
            if total > ans:
                ans = total

    print(f"#{tc} {ans}")