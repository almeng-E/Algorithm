import sys
input = sys.stdin.readline


def z(x, y, size):
    global cnt, r, c
    if size == 1:
        if x == r and y == c:
            print(cnt)
            exit()
        cnt += 1
        return
    n_size = size >> 1
    # 가지치기?
    # 1사분면
    if x <= r < x+n_size and y <= c < y+n_size:
        z(x, y, n_size)
    else:
        cnt += n_size*n_size
    # 2사분면
    if x <= r < x+n_size and y+n_size <= c < y+size:
        z(x, y+n_size, n_size)
    else:
        cnt += n_size*n_size
    # 3사분면
    if x+n_size <= r < x+size and y <= c < y+n_size:
        z(x+n_size, y, n_size)
    else:
        cnt += n_size*n_size
    # 4사분면
    if x+n_size <= r < x+size and y+n_size <= c < y+size:
        z(x+n_size, y+n_size, n_size)
    else:
        cnt += n_size*n_size

    return


N, r, c = map(int, input().split())

SIZE = 1 << N
cnt = 0
z(0, 0, SIZE)
