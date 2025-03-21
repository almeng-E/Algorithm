import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def backtrack(x, y, tmp):
    global res
    res = max(res, tmp)


    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] not in word_set:
                word_set.add(board[nx][ny])
                backtrack(nx, ny, tmp+1)
                word_set.remove(board[nx][ny])


steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))
R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

res = 0
word_set = set()
word_set.add(board[0][0])
backtrack(0, 0, 1)

print(res)