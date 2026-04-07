import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

trash = []
for i in range(N):
    for j in range(M):
        if board[i][j]:
            trash.append((i, j))
trash.sort()

robot = []

for i, j in trash:
    r_idx = -1
    closest_c = -1

    for r in range(len(robot)):
        if robot[r] <= j:
            if closest_c < robot[r]:
                r_idx = r
                closest_c = robot[r]

    if r_idx == -1:
        robot.append(j)
    else:
        robot[r_idx] = j
print(len(robot))
