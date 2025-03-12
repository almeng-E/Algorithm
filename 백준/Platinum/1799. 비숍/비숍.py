import sys
input = sys.stdin.readline


def backtrack(tmp, c_idx, board):
    global res
    if c_idx == len(board):
        res = max(tmp, res)
        return

    # 남은 후보의 합과 tmp의 합이 res 보다 작으면 가지치기
    if len(board) - c_idx + tmp <= res:
        return

    # backtrack
    nx, ny = board[c_idx]
    up_idx = nx + ny
    down_idx = ny - nx + (N-1)
    # 놓을 수 있음 (놓고 다음 호출)
    if not visited_diag_up[up_idx] and not visited_diag_down[down_idx]:
        visited_diag_up[up_idx] = True
        visited_diag_down[down_idx] = True
        backtrack(tmp + 1, c_idx + 1, board)
        visited_diag_up[up_idx] = False
        visited_diag_down[down_idx] = False

    backtrack(tmp, c_idx + 1, board)




N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

visited_diag_up = [False] * (2 * N - 1)
visited_diag_down = [False] * (2 * N - 1)

can_bishop_white = []
can_bishop_black = []
# visited 배열 처리
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            if i % 2 == j % 2:
                can_bishop_white.append((i, j))
            else:
                can_bishop_black.append((i, j))

answer = 0
res = 0
backtrack(0, 0, can_bishop_white)
answer += res
res = 0
backtrack(0, 0, can_bishop_black)
answer += res


print(answer)