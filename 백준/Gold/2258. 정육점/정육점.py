import sys
input = sys.stdin.readline
N, M = map(int, input().split())
meat = [list(map(int, input().split())) for _ in range(N)]
meat.sort(key=lambda x: (x[1], -x[0]))

ans = -1
res = []
bag = 0
cur_max_cost = -1
for w, c in meat:
    bag += w
    if cur_max_cost == c:
        ans += c
    else:
        cur_max_cost = c
        ans = c
    if bag >= M:
        res.append(ans)

if res:
    print(min(res))
else:
    print(-1)