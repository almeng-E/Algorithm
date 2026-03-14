import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append((m, s, d))

delta = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

for _ in range(K):
    n_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                continue
            for m, s, d in board[i][j]:
                di, dj = delta[d]
                ni, nj = (i+di*s)%N, (j+dj*s)%N
                n_board[ni][nj].append((m, s, d))
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not n_board[i][j]:
                continue
            if len(n_board[i][j]) == 1:
                board[i][j] = n_board[i][j]
                continue
            nm = 0
            ns = 0
            e_cnt = 0
            o_cnt = 0
            for m, s, d in n_board[i][j]:
                nm += m
                ns += s
                if d & 1:
                    o_cnt += 1
                else:
                    e_cnt += 1
            nm //= 5
            if nm == 0:
                continue
            ns //= e_cnt+o_cnt
            if e_cnt and o_cnt:
                nd = (1, 3, 5, 7)
            else:
                nd = (0, 2, 4, 6)
            for d in nd:
                board[i][j].append((nm, ns, d))


ans = 0
for i in range(N):
    for j in range(N):
        if not board[i][j]:
            continue
        for m, _, _ in board[i][j]:
            ans += m
print(ans)