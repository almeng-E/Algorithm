# 파이썬 sort, key DSU 패턴에 대해 공부할 수 있었던 좋은 문제네요

import sys
input = sys.stdin.readline
year = 1
while True:
    cmd = input().split()
    if cmd[0] == '0':
        break
    N = int(cmd[0])
    order = cmd[1]

    rank = {}
    for i in range(26):
        rank[order[i]] = i

    print(f'year {year}')
    year += 1


    words = [input().rstrip() for _ in range(N)]
    words.sort(key=lambda x: tuple(rank[c] for c in x))
    for w in words:
        print(w)