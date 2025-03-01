import sys
input = sys.stdin.readline

A, B = map(int, input().split())
res = 0


while A < B:
    if B % 2 == 0:
        B //= 2
        res += 1
        continue
    elif B % 10 == 1:
        B -= 1
        B //= 10
        res += 1
        continue
    break


if B == A:
    print(res+1)
else:
    print(-1)