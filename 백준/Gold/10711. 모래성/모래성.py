# 1등 풀이 연습...
# 와 어떻게 이런 생각을 하지?
# 문제의 요구 사항 : 0의 개수를 세서 -> 내 원래 높이 보다 많거나 같으면 0이 된다
# 를 바꿔 생각해서... 0이 되면 주위를 -1 한다...
# 발상의 전환 미쳤어요
from collections import deque
def bfs():
    # 큐 생성
    queue = deque()

    # 초기 보드 만들기
    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                board[i][j] = 0
                queue.append((i, j, 0))
            else:
                board[i][j] = int(board[i][j])

    while queue:
        x, y, wave = queue.popleft()

        # 0 이면 주위의 높이를 내리자
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                board[nx][ny] -= 1

                if board[nx][ny] == 0:  # 다음 턴에 무너짐
                    queue.append((nx, ny, wave + 1))
    return wave
steps = ((0, +1), (0, -1), (+1, 0), (-1, 0), (+1, +1), (-1, +1), (-1, -1), (+1, -1))

H, W = map(int, input().split())

board = [list(input()) for _ in range(H)]

print(bfs())