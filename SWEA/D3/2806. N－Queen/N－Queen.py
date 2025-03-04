def dfs(x, y):
    global res

    if x == (N-1):
        res += 1
        return

    # 마킹
    for dx, dy in steps:
        i = 1
        while True:
            nx, ny = x + dx*i, y + dy*i
            if not(0 <= nx < N and 0 <= ny < N): break

            visited[nx][ny] += 1
            i += 1

    # 가지치기: 다음 행에 안전한 칸이 전혀 없으면 백트래킹
    safe_exists = any(visited[x+1][j] == 0 for j in range(N))
    if safe_exists:
        for j in range(N):
            if visited[x+1][j] == 0:
                dfs(x+1, j)

    # 백트래킹
    for dx, dy in steps:
        i = 1
        while True:
            nx, ny = x + dx * i, y + dy * i
            if not (0 <= nx < N and 0 <= ny < N): break

            visited[nx][ny] -= 1
            i += 1



steps = ((+1, 0), (+1, +1), (+1, -1))
T = int(input())
for TC in range(T):
    N = int(input())

    visited = [[0 for _ in range(N)] for _ in range(N)]

    res = 0

    # 첫 줄로 체크하기
    for i in range(N):
        visited[0][i] = 1
        dfs(0, i)
        visited[0][i] = 0


    print(f'#{TC+1} {res}')