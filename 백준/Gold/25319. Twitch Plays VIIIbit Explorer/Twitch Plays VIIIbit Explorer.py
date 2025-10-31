import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
board = [list(input()) for _ in range(N)]
S = input().rstrip()
letters = {}
for i in range(N):
    for j in range(M):
        c = board[i][j]
        if c in letters:
            letters[c].append((i, j))
        else:
            letters[c] = [(i, j)]


S_cnt = {}
for c in S:
    if c in S_cnt:
        S_cnt[c] += 1
    else:
        S_cnt[c] = 1

for ch in S_cnt:
    if ch not in letters:
        moves = []
        for _ in range(N-1):
            moves.append('D')
        for _ in range(M-1):
            moves.append('R')
        path = ''.join(moves)
        print(0, len(path))
        print(path)
        exit()

max_possible = float('inf')
for k, v in S_cnt.items():
    max_possible = min(max_possible, (len(letters[k])) // v)

pos = []
for t in range(max_possible):
    for ch in S:
        nxt = letters[ch].pop()
        pos.append(nxt)
pos.append((N-1, M-1))

res = []
cx, cy = 0, 0
for nx, ny in pos:
    dx, dy = nx-cx, ny-cy

    if dx > 0:
        for _ in range(dx):
            res.append('D')
    elif dx < 0:
        for _ in range(-dx):
            res.append('U')

    if dy > 0:
        for _ in range(dy):
            res.append('R')
    elif dy < 0:
        for _ in range(-dy):
            res.append('L')

    cx, cy = nx, ny
    res.append('P')

res.pop()
print(max_possible, len(res))
print(''.join(res))