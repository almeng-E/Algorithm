def dfs(x, y, tmp, cnt):
    if cnt == 7:
        res.add(int(tmp))
        return

    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= 4 or 0 > ny or ny >= 4:
            continue
        dfs(nx, ny, tmp+board[nx][ny], cnt+1)



T = int(input())

steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))
for TC in range(T):
    board = [list(input().split()) for _ in range(4)]

    res = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, '', 0)



    print(f'#{TC+1} {len(res)}')