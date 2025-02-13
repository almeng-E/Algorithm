from copy import deepcopy
from collections import deque


def bfs(x, y, dig_i=-1, dig_j=-1, dig=0, copy=False):
    if x == dig_i and y == dig_j:
        return 0
    tmp_board = [[1 for _ in range(N)] for _ in range(N)]
    if copy:
        board = deepcopy(original_board)
        board[dig_i][dig_j] -= dig
    else:
        board = original_board
    queue = deque()
    queue.append((x, y))
    while queue:
        i, j = queue.popleft()
        current_height = board[i][j]
        for dx, dy in steps:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] < current_height:
                if tmp_board[nx][ny] <= tmp_board[i][j] + 1:
                    tmp_board[nx][ny] = tmp_board[i][j] + 1
                queue.append((nx, ny))
    # 최장 길이 찾기
    tmp = find_max(tmp_board)
    return tmp


def find_max(arr):
    tmp = 0
    for i in arr:
        max_val = max(i)
        if tmp < max_val:
            tmp = max_val
    return tmp


#           상       우        하      좌
steps = ((-1, 0), (0, +1), (+1, 0), (0, -1))

T = int(input())
for TC in range(T):
    N, K = map(int, input().split())

    result = 0

    original_board = [list(map(int, input().split())) for _ in range(N)]

    # 최고 봉우리 찾기
    max_height = find_max(original_board)

    # 최고 봉우리의 위치 찾기
    peaks = []
    for i in range(N):
        for j in range(N):
            if original_board[i][j] == max_height:
                peaks.append((i, j))

    # 각 봉우리에서 시작하여 DFS로 최대 길이 찾고 result 와 비교
    for x, y in peaks:
        tmp = bfs(x, y)
        if result < tmp:
            result = tmp

    # 땅 파고 다시 계산
    for i in range(N):
        for j in range(N):
            for k in range(1, K+1):
                for (x, y) in peaks:
                    tmp = bfs(x, y, dig_i=i, dig_j=j, dig=k, copy=True)
                    if result < tmp:
                        result = tmp
    print(f'#{TC+1} {result}')