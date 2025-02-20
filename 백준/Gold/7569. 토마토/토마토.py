def check():
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if boxes[k][i][j] == 0:
                    return -1
    return 1


# (높이, 세로, 가로)
steps = ((+1, 0, 0), (-1, 0, 0), (0, 0, +1), (0, 0, -1), (0, +1, 0), (0, -1, 0))

from collections import deque
# M 가로 N 세로 H 높이
M, N, H = map(int, input().split())

boxes = [[] for _ in range(H)]
for k in range(H):
    for _ in range(N):
        boxes[k].append(list(map(int, input().split())))

# queue 기본값 설정
queue = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[k][i][j] == 1:
                queue.append((k, i, j, 0))

tmp = 0
# BFS 실행
while queue:
    # 높이 세로 가로
    z, x, y, days = queue.popleft()
    tmp = max(tmp, days)

    for dz, dx, dy in steps:
        nz, nx, ny = z+dz, x+dx, y+dy
        if nz in (-1, H) or nx in (-1, N) or ny in (-1, M): continue
        if boxes[nz][nx][ny] in (-1, 1) : continue

        boxes[nz][nx][ny] = 1
        queue.append((nz, nx, ny, days+1))


# 0 여부 체크
res = check()

# 출력
print(res if res == -1 else tmp)