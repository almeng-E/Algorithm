import heapq
import sys
input = sys.stdin.readline

steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))
INF = float('inf')
TC = 0
while True:
    TC += 1
    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF for _ in range(N)] for _ in range(N)]

    hq = []
    distance[0][0] = board[0][0]
    heapq.heappush(hq, (board[0][0], 0, 0)) # 현재거리, 좌표 x, y

    while hq:
        q_dist, cx, cy = heapq.heappop(hq)

        if distance[cx][cy] < q_dist: continue

        for dx, dy in steps:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] > q_dist + board[nx][ny]:
                distance[nx][ny] = q_dist + board[nx][ny]
                heapq.heappush(hq, (distance[nx][ny], nx, ny))

    print(f'Problem {TC}: {distance[N - 1][N - 1]}')
