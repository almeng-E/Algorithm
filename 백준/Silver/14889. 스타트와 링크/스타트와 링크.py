from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

used = set()
res = float('inf')
nCr = combinations(range(N), N//2)
for team in nCr:
    if team in used:
        continue
    opponent = set(range(N)) - set(team)

    used.add(team)
    used.add(tuple(opponent))

    t_sc = 0
    for i in team:
        for j in team:
            t_sc += board[i][j]
    o_sc = 0
    for i in opponent:
        for j in opponent:
            o_sc += board[i][j]

    res = min(res, abs(o_sc - t_sc))
print(res)