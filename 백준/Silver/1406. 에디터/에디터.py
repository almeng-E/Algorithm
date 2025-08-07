import sys
input = sys.stdin.readline

class Char:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.v = v


F = Char(0)
E = Char(0)

cursor = Char(1)
F.right = cursor
cursor.left = F
cursor.right = E
E.left = cursor

bef = F

SS = input().rstrip()

for s in SS:
   cur = Char(s)
   bef.right = cur
   cur.left = bef
   bef = cur
bef.right = cursor
cursor.left = bef


M = int(input())
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        if cursor.left.v == 0:  # F 확인
            continue
        L = cursor.left
        R = cursor.right
        L.right = R
        R.left = L

        cursor.left = L.left
        cursor.right = L
        cursor.left.right = cursor
        L.left = cursor

    elif cmd[0] == 'D':
        if cursor.right.v == 0:  # E 확인
            continue
        L = cursor.left
        R = cursor.right
        L.right = R
        R.left = L

        cursor.right = R.right
        cursor.left = R
        cursor.right.left = cursor
        R.right = cursor

    elif cmd[0] == 'B':
        if cursor.left.v == 0:  # F 확인
            continue
        L = cursor.left

        L.left.right = cursor
        cursor.left = L.left

    elif cmd[0] == 'P':
        c = Char(cmd[1])

        L = cursor.left
        L.right = c
        c.left = L
        c.right = cursor
        cursor.left = c

cur = F.right
while cur.v != 0:
    if cur.v != 1:
        print(cur.v, end="")
    cur = cur.right



