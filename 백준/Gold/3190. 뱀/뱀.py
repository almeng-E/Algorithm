from collections import deque


N = int(input())

K = int(input())
# 사과의 위치 (행 , 열) 인덱스 1부터임 주의
apples = set()
for _ in range(K):
    apples.add(tuple(map(int, input().split())))
# 뱀 방향 전환 횟수
L = int(input())
# 방향 전환 정보 : 정수 X 문자 C ... L/D ... X 초 후
turns = [input().split() for _ in range(L)]

turns = deque(turns)

my_snake = deque()
cx, cy = 1, 1
my_snake.append((cx, cy))
sec = 0
#  우    하   좌   상
steps = ((0, +1), (+1, 0), (0, -1), (-1, 0))
di = 0
while True:
    sec += 1
    # 머리 늘리기
    cx = cx+steps[di][0]
    cy = cy+steps[di][1]

    # 벽 / 몸 : 게임 끝
    if (cx, cy) in my_snake or cx == 0 or cx == N+1 or cy == 0 or cy == N+1:
        break
    my_snake.append((cx, cy))
    # 이동하고 꼬리 떼기
    if (cx, cy) not in apples:
        my_snake.popleft()
    else:
        apples.remove((cx, cy))

    # 방향 전환
    if turns:
        if sec == int(turns[0][0]):
            if turns[0][1] == 'L':
                di = (di-1)%4
            else:
                di = (di+1)%4
            turns.popleft()

print(sec)