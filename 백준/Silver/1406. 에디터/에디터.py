import sys
input = sys.stdin.readline



LS = list(input().rstrip())
RS = []

M = int(input())
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        if not LS:
            continue
        cc = LS.pop()
        RS.append(cc)

    elif cmd[0] == 'D':
        if not RS:
            continue
        cc = RS.pop()
        LS.append(cc)

    elif cmd[0] == 'B':
        if not LS:
            continue
        LS.pop()

    elif cmd[0] == 'P':
        LS.append(cmd[1])

for c in LS:
    print(c, end="")
for c in reversed(RS):
    print(c, end="")