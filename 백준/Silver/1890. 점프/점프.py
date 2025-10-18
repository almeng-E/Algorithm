import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x, y):
    if (x, y) == (N-1, N-1):
        return 1

    if memo[x][y] == -1:
        memo[x][y] = 0
        cur = memo[x][y]
    else:
        return memo[x][y]

    v = board[x][y]
    for dx, dy in steps:
        dx *= v
        dy *= v
        nx, ny = x+dx, y+dy
        if nx >= N or ny >= N: continue
        cur += dfs(nx, ny)
    memo[x][y] = cur
    return cur


steps = ((0, 1), (1, 0))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
memo = [[-1 for _ in range(N)] for _ in range(N)]
# memo[0][0] = 0

dfs(0, 0)
print(memo[0][0])