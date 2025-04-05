import sys
input = sys.stdin.readline


N = int(input())

time = [0] * (N+1)


for i in range(1, N+1):
    t, _, *post = map(int, input().split())
    tmp = 0
    for p in post:
        if tmp < time[p]:
            tmp = time[p]
    time[i] = t + tmp

print(max(time))