
from itertools import combinations, product


def checker(board):
    res = 0
    for j in range(W):
        cnt = 1
        tmp = board[0][j]
        for i in range(1, D):
            if tmp == board[i][j]:
                cnt += 1
            else:
                tmp = board[i][j]
                cnt = 1
            if cnt >= K:
                res += 1
                break
    if res == W:
        return True
    else:
        return False


def change_chemical_and_check(comb, prod):
    injection = dict(zip(comb, prod))
    for j in range(W):
        cnt = 1
        # 첫 번째 행의 값: injection에 있으면 해당 약품, 아니면 원래 board 값.
        val = injection.get(0, board[0][j])
        for i in range(1, D):
            cur = injection.get(i, board[i][j])
            if cur == val:
                cnt += 1
            else:
                cnt = 1
                val = cur
            if cnt >= K:
                break
        else:
            return False
    return True


def put_chem_and_check():
    global res
    # nCr로 투약
    # 개수
    for i in range(1, D + 1):
        # comb : (0, 1, 2) ...
        for comb in combinations(range(D), i):
            # prod : (a, a, b) ...
            for prod in product((0, 1), repeat=len(comb)):
                if change_chemical_and_check(comb, prod):
                    res = len(comb)
                    return res


T = int(input())
for TC in range(T):
    # D: 두께, W: 가로, K: 합격기준
    D, W, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(D)]

    # 열 체크
    if K == 1 or checker(board):
        res = 0
    else:
        res = put_chem_and_check()

    print(f'#{TC + 1} {res}')