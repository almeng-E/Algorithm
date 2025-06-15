import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    sub = [0]
    tmp = 0
    for i in arr:
        tmp += i
        sub.append(tmp)

    res = -float('inf')
    for i in range(N+1):
        for j in range(i):
            res = max(sub[i]-sub[j], res)
    print(res)