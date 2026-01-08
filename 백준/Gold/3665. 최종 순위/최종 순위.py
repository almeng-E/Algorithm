import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    order = [0] + list(map(int, input().split()))
    last_year = [0] * (N+1)
    for i in range(1, N+1):
        last_year[order[i]] = i
    points = [0] * (N+1)
    for i in range(1, N+1):
        points[i] = last_year[i] - 1
    M = int(input())
    changed = []
    for _ in range(M):
        a, b = map(int, input().split())
        if last_year[a] < last_year[b]:
            a, b = b, a
        points[a] -= 1
        points[b] += 1
    this_year = [0] * (N+1)
    for i in range(1, N+1):
        idx = N - points[i]
        if this_year[idx] != 0:
            print('IMPOSSIBLE')
            break
        else:
            this_year[idx] = i
    else:
        print(*this_year[:0:-1])