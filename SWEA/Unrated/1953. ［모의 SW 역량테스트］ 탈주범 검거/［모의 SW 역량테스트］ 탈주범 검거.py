from collections import deque

#            상       우       하       좌
steps = ((-1, 0), (0, +1), (+1, 0), (0, -1))

can_go = {          # 터널 번호 : 갈 수 있는 방향 인덱스         ... 여기 안에 있으면 진입 불가
    1: (0, 1, 2, 3),
    2: (0, 2),      # 여기서부터는 진입 방향 체크 필요
    3: (1, 3),
    4: (0, 1),
    5: (1, 2),
    6: (2, 3),
    7: (0, 3)
}

can_come = {    # 터널 번호 : 진입 가능한 방향들
    1: (0, 1, 2, 3),
    2: (0, 2),
    3: (1, 3),
    4: (2, 3),
    5: (0, 3),
    6: (0, 1),
    7: (1, 2)
}


T = int(input())
for TC in range(T):
    # 세로 크기 N | 가로 크기 M | 맨홀 뚜껑이 위치한장소의 세로 위치 R |  가로 위치 C | 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())


    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((R, C, 1))
    time = 1


    while queue:
        x, y, time = queue.popleft()
        # 최댓값으로 갱신
        if visited[x][y] < time:
            visited[x][y] = time
        else:
            continue

        if time == L:
            continue

        c_pipe = board[x][y]
        poss_dir = can_go[c_pipe]

        # 다음 방향 찾고 탐색 고민
        for direction in poss_dir:
            dx, dy = steps[direction]
            nx, ny = x + dx, y + dy

            # 못 가는 경우들
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if board[nx][ny] == 0: continue
            if direction not in can_come[board[nx][ny]]: continue

            # GO !
            queue.append((x, y, time+1))    # 가만히 있기
            queue.append((nx, ny, time+1))


    res = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == L:
                res += 1

    print(f'#{TC+1} {res}')