import sys
input = sys.stdin.readline


N, M = map(int, input().split())
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1
def solve():
    tree_board = [[0 for _ in range(SIZE)] for _ in range(N)]
    
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(N):
            tree_board[i][j + LEN] = arr[j]
    
        for j in range(LEN-1, 0, -1):
            tree_board[i][j] = tree_board[i][j*2] + tree_board[i][j*2 + 1]
    
    for _ in range(M):
        cmd = list(map(int, input().split()))
    
        if cmd[0] == 0:
            _, x, y, c = cmd
            idx = y - 1 + LEN
            tree_board[x-1][idx] = c
            idx >>= 1
            while idx:
                tree_board[x-1][idx] = tree_board[x-1][idx*2] + tree_board[x-1][idx*2 + 1]
                idx >>= 1
    
        else:
            _, x1, y1, x2, y2 = cmd
            ret = 0
    
            left = y1 - 1 + LEN
            right = y2 - 1 + LEN
    
            while left <= right:
                if left & 1:
                    for i in range(x1-1, x2):
                        ret += tree_board[i][left]
                    left += 1
    
                if not (right & 1):
                    for i in range(x1-1, x2):
                        ret += tree_board[i][right]
                    right -= 1
    
                left >>= 1
                right >>= 1
    
            print(ret)
    
solve()