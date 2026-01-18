import sys
input = sys.stdin.readline
N = int(input())
vil = [tuple(map(int, input().split())) for _ in range(N)]
INF = float('inf')
ans = INF
d = [[INF, INF] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        tmp = 0
        for k in range(3):
            tmp += abs(vil[i][k] - vil[j][k])

        if d[i][1] <= tmp:
            pass
        elif d[i][0] <= tmp < d[i][1]:
            d[i][1] = tmp
        else:
            d[i][1] = d[i][0]
            d[i][0] = tmp


        if d[j][1] <= tmp:
            pass
        elif d[j][0] <= tmp < d[j][1]:
            d[j][1] = tmp
        else:
            d[j][1] = d[j][0]
            d[j][0] = tmp


for r in d:
    ans = min(ans, sum(r))
print(ans)