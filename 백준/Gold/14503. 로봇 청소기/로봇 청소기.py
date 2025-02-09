import sys
input = sys.stdin.readline


def check(i, j, room):
    global direction, steps
    for dx, dy in steps:
        if 0 <+ i+dx < N and 0 <= j+dy < M:
            if room[i+dx][j+dy] == 0:
                return True
    return False


# 인덱스 0,0 ~ n-1,m-1 ... 그대로 사용 and 출력
# 0이면 더러움, 1은 벽         ==> 청소됨 2
N, M = map(int, input().split())
R, C, D = map(int, input().split())
#           북 동 남 서
steps = ((-1, 0 ), (0, +1), (+1, 0), (0, -1))

room = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
i, j = R, C
while True:
    # 현재 칸 청소
    if room[i][j] == 0:
        cnt += 1
        room[i][j] = 2

    # 4방향 탐색
    # 더러운 방이 있으면
    if check(i, j, room):
        for _ in range(4):
            # d 변경
            D -= 1
            if D == -1:
                D = 3
            # 회전 후 앞 더러우면 go
            if room[i + steps[D][0]][j + steps[D][1]] == 0:
                i = i + steps[D][0]
                j = j + steps[D][1]
                break
            # 아니면 계속 변경
            else:
                continue
        continue
    # 없으면
    else:
        # 후진 할 수 없으면 break
        if room[i - steps[D][0]][j - steps[D][1]] == 1:
            break
        # 후진
        else:
            i = i - steps[D][0]
            j = j - steps[D][1]
            continue
print(cnt)



