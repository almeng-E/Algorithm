import sys
input = sys.stdin.readline
from collections import deque

def search():
    global x, y, OIL

    q = deque()
    q.append((x, y))
    v = [[-1 for _ in range(N)] for _ in range(N)]
    v[x][y] = 0

    candidates = []
    while q:
        cx, cy = q.popleft()
        if board[cx][cy] < 0:
            p_id = -board[cx][cy] - 1
            candidates.append((v[cx][cy], cx, cy, p_id))
        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy
            if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 1 or v[nx][ny] != -1:
                continue

            v[nx][ny] = v[cx][cy] + 1
            q.append((nx, ny))

    if not candidates:
        return -1

    candidates.sort()
    dist, px, py, p_id = candidates[0]
    if dist > OIL:
        return -1
    OIL -= dist
    x, y = px, py
    board[px][py] = 0
    return p_id


def move(p_id):
    global x, y, OIL
    tx, ty = target[p_id]
    q = deque()
    q.append((x, y))
    v = [[-1 for _ in range(N)] for _ in range(N)]
    v[x][y] = 0
    while q:
        cx, cy = q.popleft()
        if (cx, cy) == (tx, ty):
            dist = v[cx][cy]
            if dist > OIL:
                return False

            OIL -= dist
            OIL += dist*2

            x, y = tx, ty
            done[p_id] = 1
            return True

        for dx, dy in delta:
            nx, ny = cx+dx, cy+dy
            if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 1 or  v[nx][ny] != -1:
                continue
            v[nx][ny] = v[cx][cy]+1
            q.append((nx, ny))
    return False


N, M, OIL = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
x -= 1
y -= 1
target = []
for p_idx in range(M):
    px, py, tx, ty = map(int, input().split())
    board[px-1][py-1] = -(p_idx + 1)
    target.append((tx-1, ty-1))

delta = ((-1, 0), (0, -1), (0, 1), (1, 0))
done = [0] * M


while sum(done) != M:
    # 다음 손님 찾기
    p_id = search()
    if p_id == -1:
        OIL = -1
        break

    # 이동하기
    success = move(p_id)
    if not success:
        OIL = -1
        break

print(OIL)