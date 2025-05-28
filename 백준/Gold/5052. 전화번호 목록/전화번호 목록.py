import sys
input = sys.stdin.readline
class Node:
    def __init__(self):
        self.is_terminal = False
        self.child = {}

def sol():
    N = int(input())
    arr = list(input().rstrip() for _ in range(N))

    for num in arr:
        cur = ROOT
        for s in num:
            if s not in cur.child:
                cur.child[s] = Node()

            if cur.is_terminal:
                return False

            cur = cur.child[s]
        if cur.child:
            return False
        cur.is_terminal = True

    return True


T = int(input())

for _ in range(T):
    ROOT = Node()
    res = sol()
    print('YES' if res else 'NO')