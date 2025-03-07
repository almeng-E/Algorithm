from collections import deque
from itertools import product
from copy import deepcopy
 
 
def boom(drop_point, boom_board):
    queue = deque()
 
    # 이번 팡팡의 sx, sy 값 찾기
    sx = drop_point
    for i in range(H-1, -1, -1):
        if boom_board[sx][i] != 0:
            sy = i
            break
    else:
        # 빈 줄
        return
    current_power = boom_board[sx][sy]
    queue.append((sx, sy, current_power))
    boom_board[sx][sy] = 0
    while queue:
        x, y, current_power = queue.popleft()
        for dx, dy in steps:
            for i in range(1, current_power):
                nx = x + dx*i
                ny = y + dy*i
                # 인덱스 범위 내 인지 확인
                if nx < 0 or nx >= W or ny < 0 or ny >= H:
                    break
                # 0이면 continue
                if boom_board[nx][ny] == 0:
                    continue
                if boom_board[nx][ny] > 1:
                    queue.append((nx, ny, boom_board[nx][ny]))
                boom_board[nx][ny] = 0
 
 
    # 떨어지는 로직
    for i in range(W):
        tmp_line = []
        for j in range(H):
            if boom_board[i][j] != 0:
                tmp_line.append(boom_board[i][j])
        boom_board[i][:] = tmp_line + [0] * (H - len(tmp_line))
 
 
#          상       하       좌      우
steps = ((-1, 0), (+1, 0), (0, -1), (0, +1))
 
T = int(input())
for TC in range(T):
    # N 공 개수, W 가로 H 높이
    N, W, H = map(int, input().split())
 
    board_input = [list(map(int, input().split())) for _ in range(H)]
    # 보드는 이제 90도 회전하여 관리
    board = [[] for _ in range(W)]
    for j in range(W):
        for i in range(H-1, -1, -1):
            board[j].append(board_input[i][j])
 
    # 후보
    nHr = product(range(W), repeat=N)
    # 전체 탐색
    res = 12*15
    for trial in nHr:
        boom_board = deepcopy(board)
        for drop_point in trial:
            boom(drop_point, boom_board)
 
        # 이후 전체 개수 확인
        check = 0
        for i in range(W):
            for j in range(H):
                if boom_board[i][j] != 0:
                    check += 1
 
        res = min(res, check)
        if res == 0:
            break
 
 
    print(f'#{TC+1} {res}')