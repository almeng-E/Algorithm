import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())

    f = list(map(int, input().rstrip()))
    s = list(input().rstrip())

    for i in range(N):
        if s[i] == '*':
            if i - 1 >= 0: f[i - 1] -= 1
            f[i] -= 1
            if i + 1 < N: f[i + 1] -= 1

    for i in range(N):
        if s[i] == '#':
            can_place = True

            if i - 1 >= 0 and f[i - 1] <= 0: can_place = False
            if f[i] <= 0: can_place = False
            if i + 1 < N and f[i + 1] <= 0: can_place = False

            if can_place:
                s[i] = '*'
                if i - 1 >= 0: f[i - 1] -= 1
                f[i] -= 1
                if i + 1 < N: f[i + 1] -= 1

    print(s.count('*'))
