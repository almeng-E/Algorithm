# 방향으로 밀고 합치기
def swipe(direction):
    # 위로 올리기
    if direction == 'up':
        for j in range(N):
            tmp_li = []
            # 밀고
            for i in range(N):
                cell = board[i][j]
                if cell > 0:
                    tmp_li.append(cell)
            # 합치고
            if len(tmp_li) > 1:
                tmp_li = merge(tmp_li)

            # 원래 보드에 업데이트
            for i in range(N):
                if i < len(tmp_li):
                    board[i][j] = tmp_li[i]
                else:
                    board[i][j] = 0

    # 왼쪽으로 밀기
    elif direction == 'left':
        for i in range(N):
            tmp_li = []
            # 밀고
            for j in range(N):
                cell = board[i][j]
                if cell > 0:
                    tmp_li.append(cell)
            # 합치고
            if len(tmp_li) > 1:
                tmp_li = merge(tmp_li)

            # 원래 보드에 업데이트
            for j in range(N):
                if j < len(tmp_li):
                    board[i][j] = tmp_li[j]
                else:
                    board[i][j] = 0

    # 아래로 밀기
    elif direction == 'down':
        for j in range(N):
            tmp_li = []
            # 밀고
            for i in range(N):
                cell = board[N-i-1][j]
                if cell > 0:
                    tmp_li.append(cell)
            # 합치고
            if len(tmp_li) > 1:
                tmp_li = merge(tmp_li)

            # 원래 보드에 업데이트
            for i in range(N):
                if i < len(tmp_li):
                    board[N-i-1][j] = tmp_li[i]
                else:
                    board[N-i-1][j] = 0

    # 오른쪽으로 밀기
    elif direction == 'right':
        for i in range(N):
            tmp_li = []
            # 밀고
            for j in range(N):
                cell = board[i][N-j-1]
                if cell > 0:
                    tmp_li.append(cell)
            # 합치고
            if len(tmp_li) > 1:
                tmp_li = merge(tmp_li)

            # 원래 보드에 업데이트
            for j in range(N):
                if j < len(tmp_li):
                    board[i][N-j-1] = tmp_li[j]
                else:
                    board[i][N-j-1] = 0

# 다음 칸과 비교해서 칸 병합하기
def merge(li):
    merged_li = [li[0]]
    for i in range(1, len(li)):
        if li[i] == li[i-1] and li[i] == merged_li[-1]:
            merged_li[-1] *= 2
        else:
            merged_li.append(li[i])

    return merged_li




T = int(input())
for TC in range(T):
    N, S = input().split()
    N = int(N)

    board = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{TC+1}')
    swipe(S)
    for row in board:
        print(*row)