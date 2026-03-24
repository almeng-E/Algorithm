import sys
input = sys.stdin.readline

while True:
    p = int(input())
    if p == 0:
        break

    S = input().split(',')
    for i in range(len(S)):
        S[i] = list(map(int, S[i].split('-')))
    ans = [0] * (p+1)
    for pgs in S:
        if len(pgs) == 1:
            if pgs[0] <= p:
                ans[pgs[0]] = 1
        else:
            a, b = pgs
            for i in range(a, min(b+1, p+1)):
                ans[i] = 1

    print(sum(ans))
    