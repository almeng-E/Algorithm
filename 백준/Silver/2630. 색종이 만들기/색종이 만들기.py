import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def quad(sx, sy, size):
    global N
    if sx >= N or sy >= N:
        return 2
    if size == 1:
        return board[sx][sy]
    ns = size//2
    s1 = quad(sx, sy, ns)
    s2 = quad(sx, sy+ns, ns)
    s3 = quad(sx+ns,sy, ns)
    s4 = quad(sx+ns, sy+ns, ns)

    if s1 == s2 == s3 == s4:
        return s1
    else:
        if s1 != 2:
            cnt[s1] += 1
        if s2 != 2:
            cnt[s2] += 1
        if s3 != 2:
            cnt[s3] += 1
        if s4 != 2:
            cnt[s4] += 1
        return 2


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0]    # white, blue

quad(0, 0, 2*N)
print(cnt[0])
print(cnt[1])