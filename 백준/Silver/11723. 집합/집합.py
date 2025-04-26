import sys
input = sys.stdin.readline
my = 0
for _ in range(int(input())):
    C = input().split()
    if C[0] == 'add':
        my |= (1 << int(C[1]))
    elif C[0] == 'remove':
        my &= ~(1 << int(C[1]))
    elif C[0] == 'check':
        print(1 if (my & (1 << int(C[1]))) else 0)
    elif C[0] == 'toggle':
        my ^= (1 << int(C[1]))
    elif C[0] == 'all':
        my = (1 << 21) - 1
    else:
        my = 0