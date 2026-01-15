import sys
input = sys.stdin.readline
def recur(x, y, size):
    if size == 1:
        return board[x][y]

    ns = size // 3
    tmp = []
    for i in range(3):
        for j in range(3):
            tmp.append(recur(x+(i*ns), y+(j*ns), ns))

    if len(set(tmp)) == 1:
        return tmp[0]
    else:
        for v in tmp:
            cnt[v] += 1
        return 2


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0, 0, 0]     # 0, 1, _2_, -1
cnt[recur(0, 0, N)] += 1

print(cnt[-1])
print(cnt[0])
print(cnt[1])