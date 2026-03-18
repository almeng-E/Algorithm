import sys
input = sys.stdin.readline
def solve():
    def find_bomb_idx(x, y, dx, dy, idx):
        while True:
            x += dx
            y += dy
            if x < 0 or x >= N or y < 0 or y >= N:
                return
            bomb_idx[idx].append(order[x][y])


    N, M = map(int, input().split())

    order = [[0 for _ in range(N)] for _ in range(N)]
    delta = ((0, -1, 1), (1, 0, 0), (0, 1, 1), (-1, 0, 0))
    board = [list(map(int, input().split())) for _ in range(N)]
    arr = [4]

    d = 0
    x, y, s = N//2, N//2, 0
    cnt = 1
    while cnt < N**2:
        dx, dy, ds = delta[d]
        s += ds
        for _ in range(s):
            x += dx
            y += dy
            order[x][y] = cnt
            cnt += 1
            if board[x][y] != 0:
                arr.append(board[x][y])
            if cnt == N**2:
                break
        d += 1
        d %= 4

    bomb_idx = [[], [], [], [], []]
    sx, sy = N//2, N//2
    find_bomb_idx(sx, sy, -1, 0, 1)
    find_bomb_idx(sx, sy, 1, 0, 2)
    find_bomb_idx(sx, sy, 0, -1, 3)
    find_bomb_idx(sx, sy, 0, 1, 4)

    ans = 0
    for _ in range(M):
        d, s = map(int, input().split())
        # 파괴 + 이동
        # ↑, ↓, ←, →
        idx = bomb_idx[d][:s]
        while idx and len(arr) < idx[-1] + len(idx):
            idx.pop()
        for i in range(len(idx)):
            arr.pop(idx[i] - i)

        # 폭발(연쇄)
        while True:
            cnt = [[4, 1]]
            for i in range(1, len(arr)):
                if arr[i] != cnt[-1][0]:
                    cnt.append([arr[i], 1])
                else:
                    cnt[-1][1] += 1
            new_arr = []
            for v, c in cnt:
                if c >= 4:
                    ans += v*c
                    continue
                for _ in range(c):
                    new_arr.append(v)
            if len(new_arr) == len(arr):
                break
            arr = new_arr

        # 복제
        new_arr = [4]
        for i in range(1, len(cnt)):
            v, c = cnt[i]
            new_arr.append(c)
            new_arr.append(v)
        arr = new_arr[:N**2]

    print(ans)
solve()