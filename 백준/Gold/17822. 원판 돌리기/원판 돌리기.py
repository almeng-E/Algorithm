import sys
input = sys.stdin.readline

from collections import deque

N, M, T = map(int, input().split())
board = [deque(list(map(int, input().split()))) for _ in range(N)]

steps = ((+1, 0), (-1, 0), (0, +1), (0, -1))



for _ in range(T):
    x, d, k = map(int, input().split())
    # di 방향 : 0 시계방향 1 반시계
    # xi-1 배수인 원판을 ki 칸 회전
    k %= M

    for i in range(N):
        # 회전
        if (i+1) % x == 0:
            for _ in range(k):
                # 시계:
                if d == 0:
                    board[i].appendleft(board[i].pop())
                # 반시계:
                else:
                    board[i].append(board[i].popleft())
    # 삭제
    change_avg = True
    copy_board = [row.copy() for row in board]
    for x in range(N):
        for y in range(M):
            # 사방 탐색
            if copy_board[x][y] == 0:
                continue
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                # 인덱스 처리
                if nx == -1:
                    continue
                elif nx == N:
                    continue
                if ny == -1:
                    ny = M-1
                elif ny == M:
                    ny = 0
                # 0 처리
                if copy_board[nx][ny] == copy_board[x][y]:
                    board[nx][ny] = 0
                    if change_avg:
                        board[x][y] = 0
                        change_avg = False

    # 삭제 못한 경우
    if change_avg:
        avg = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    avg += board[i][j]
                    cnt += 1
        if cnt > 0:
            avg /= cnt
        else:
            avg = 0
        # 평균에 대비하여 계산.
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    continue
                if board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1

res = 0
for row in board:
    res += sum(row)

print(res)