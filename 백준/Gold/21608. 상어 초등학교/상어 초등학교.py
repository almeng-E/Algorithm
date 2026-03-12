import sys
input = sys.stdin.readline


N = int(input())
stud = []
for _ in range(N**2):
    s_id, *fav = map(int, input().split())
    stud.append([s_id, set(fav)])

DELTA = ((0, 1), (1, 0), (-1, 0), (0, -1))

board = [[0 for _ in range(N)] for _ in range(N)]

for idx in range(N**2):
    s_id, fav = stud[idx][0], stud[idx][1]
    max_fav_cnt = -1
    max_blank_cnt = -1
    x, y = 0, 0

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            cur_f_cnt = 0
            cur_b_cnt = 0
            for di, dj in DELTA:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                if board[ni][nj] == 0:
                    cur_b_cnt += 1
                elif board[ni][nj] in fav:
                    cur_f_cnt += 1
            if max_fav_cnt < cur_f_cnt:
                max_fav_cnt = cur_f_cnt
                max_blank_cnt = cur_b_cnt
                x, y = i, j
                continue
            if max_fav_cnt == cur_f_cnt and max_blank_cnt < cur_b_cnt:
                max_fav_cnt = cur_f_cnt
                max_blank_cnt = cur_b_cnt
                x, y = i, j
                continue
    board[x][y] = s_id
    stud[idx].append(x)
    stud[idx].append(y)

ans = 0

for s_id, fav, x, y in stud:
    cnt = 0
    for dx, dy in DELTA:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] in fav:
            cnt += 1

    if cnt != 0:
        ans += 10 ** (cnt-1)
print(ans)