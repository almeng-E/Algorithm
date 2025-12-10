import sys
input = sys.stdin.readline



class Node:
    def __init__(self, pos):
        self.bef = None
        self.nxt = None
        self.pos = pos
        self.occupied = False


N = int(input())
V = dict()

L = Node(0)
R = Node(100_001)
S = Node(1)

L.nxt = S
S.nxt = R
R.bef = S
S.bef = L
TRASH = Node(0)

L.occupied = True
R.occupied = True

for _ in range(N):
    cmd = input().rstrip()
    if cmd[4] == '=':
        var = cmd[:4]
        size = int(cmd[12:-2])
        cur = S
        while cur.nxt is not None:
            if not cur.occupied and cur.nxt.pos - cur.pos >= size:
                # 생성
                ins = Node(cur.pos + size)
                V[var] = cur
                cur.nxt.bef = ins
                ins.nxt = cur.nxt
                cur.nxt = ins
                ins.bef = cur
                cur.occupied = True
                break
            else:
                cur = cur.nxt
        else:
            V[var] = TRASH

    elif cmd[4] == '(':
        var = cmd[5:-2]
        cur = V.get(var, TRASH)
        if cur == TRASH:
            continue

        V[var] = TRASH
        cur.occupied = False

        while cur.nxt is not None and not cur.nxt.occupied:
            nxt = cur.nxt
            cur.nxt = nxt.nxt
            if nxt.nxt is not None:
                nxt.nxt.bef = cur

        if cur.bef is not None and not cur.bef.occupied:
            bef = cur.bef
            bef.nxt = cur.nxt
            if cur.nxt is not None:
                cur.nxt.bef = bef

    else:
        var = cmd[6:-2]
        out = V.get(var, TRASH)
        print(out.pos)