# 개수 체크 (count)
def check(num_list):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in num_list:
        counter[i-1] += 1
        if counter[i-1] == 2:
            return False
    return True
 
 
# 가로 체크
def hori(board):
    for line in board:
        if not check(line):
            return False
    return True
 
 
# 세로 체크
def verti(board):
    for j in range(9):
        line = []
        for i in range(9):
            line.append(board[i][j])
        if not check(line):
            return False
    return True
 
# 격자 체크
def square(board):
    for plus_y in range(0, 9, 3):       # 0 3 6
        for plus_x in range(0, 9, 3):   # 0 3 6
            line = []
            for i in range(3):          # [0~2][   ]
                for j in range(3):      # [   ][0~2]
                    line.append(board[i+plus_y][j+plus_x])
            if not check(line):
                return False
    return True
 
 
t = int(input())
for tc in range(t):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
 
    # 스도쿠 체크 및 결과 출력
    if hori(sudoku) and verti(sudoku) and square(sudoku):
        print(f'#{tc + 1} 1')
    else:
        print(f'#{tc + 1} 0')