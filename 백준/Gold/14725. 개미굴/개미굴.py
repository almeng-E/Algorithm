import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.is_terminal = False
        self.child = {}


def dfs(cur, d):
    if cur.is_terminal:
        return

    for nx in sorted(cur.child.keys()):
        print('--'*d+nx)
        dfs(cur.child[nx], d+1)



N = int(input())
ROOT = Node()

for _ in range(N):
    _, *arr = input().split()
    cur = ROOT
    for s in arr:
        if s not in cur.child:
            cur.child[s] = Node()
        cur = cur.child[s]

    cur.is_terminal = True

dfs(ROOT, 0)