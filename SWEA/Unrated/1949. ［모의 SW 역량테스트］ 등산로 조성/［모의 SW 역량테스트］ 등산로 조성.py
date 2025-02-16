
def dfs(i, j, can_dig, tmp):
    # board, visited, steps, K
    global res, K
    tmp += 1
    if res < tmp:
        res = tmp

    current_height = board[i][j]
    for dx, dy in steps:
        nx = i + dx
        ny = j + dy
        # 조기 종료 조건 설정
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if visited[nx][ny]: continue

        next_height = board[nx][ny]

        # 기존 높이보다 크거나 같으면 ==> can dig 확인...
        if next_height >= current_height and can_dig and next_height - current_height < K:
            # 땅파고 dfs
            # 들어갈 때 문 열고
            can_dig = False
            board[nx][ny] = current_height - 1
            visited[nx][ny] = True
            dfs(nx, ny, can_dig, tmp)
            # 나올 때 문 닫기
            visited[nx][ny] = False
            board[nx][ny] = next_height
            can_dig = True
        if next_height < current_height:
            # 모든 조건에 맞으면 GO !
            # 들어갈 때 문 열고
            visited[nx][ny] = True
            dfs(nx, ny, can_dig, tmp)
            # 나올 때 문 닫기
            visited[nx][ny] = False



#           상       우       하       좌
steps = ((-1, 0), (0, +1), (+1, 0), (0, -1))

T = int(input())

for TC in range(T):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]


    # 가장 높은 봉우리 찾기
    peaks = []
    highest_h = max(map(max, board))
    for i in range(N):
        for j in range(N):
            if board[i][j] == highest_h:
                peaks.append((i, j))


    # 실행
    res = 0
    for i, j in peaks:
        # 방문 처리 (갇힘 현상 방지)
        visited[i][j] = True
        dfs(i, j, True, 0)
        visited[i][j] = False


    print(f'#{TC+1} {res}')
