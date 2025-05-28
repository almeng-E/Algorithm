import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.is_terminal = False
        self.child = {}


N, M = map(int, input().split())
ROOT = Node()

# 트라이 생성
for _ in range(N):
    word = input().rstrip()
    cur = ROOT
    for s in word:
        if s not in cur.child:
            cur.child[s] = Node()

        cur = cur.child[s]

    cur.is_terminal = True

# 접두사 검사
res = 0
for _ in range(M):
    word = input().rstrip()
    cur = ROOT
    for s in word:
        if s not in cur.child:
            break
        cur = cur.child[s]
    else:
        res += 1

print(res)