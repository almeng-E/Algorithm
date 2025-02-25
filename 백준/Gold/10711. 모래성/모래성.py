from collections import deque

steps = ((0, +1), (0, -1), (+1, 0), (-1, 0), (+1, +1), (-1, +1), (-1, -1), (+1, -1))

H, W = map(int, input().split())

board = [list(input()) for _ in range(H)]

# 초기 보드 만들기
for i in range(H):
    for j in range(W):
        if board[i][j] == '.':
            board[i][j] = 0
        else:
            board[i][j] = int(board[i][j])

# 방문 체크하기
visited = [[False for _ in range(W)] for _ in range(H)]

# 큐 생성
queue = deque()

# 초기 카운트 보드 생성
count_board = [[0 for _ in range(W)] for _ in range(H)]
for i in range(1, H-1):
    for j in range(1, W-1):
        tmp = 0
        for dx, dy in steps:
            nx, ny = i + dx, j + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
                tmp += 1
        count_board[i][j] = tmp
        # 초기 queue 설정
        if 0 < board[i][j] <= tmp:
            queue.append((i, j))
            visited[i][j] = True

depth = 0
while queue:
    next_queue = deque()

    depth += 1
    for _ in range(len(queue)):
        x, y = queue.popleft()

        # 한 단계를 전부 처리
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
                count_board[nx][ny] += 1


                # 올린애들만 체크하면 되니 확인하고 다음 큐에 넣기
                if not visited[nx][ny] and 0 < board[nx][ny] <= count_board[nx][ny]:
                    visited[nx][ny] = True
                    next_queue.append((nx, ny))

    # 다음 큐 만들기
    queue = next_queue

print(depth)
