import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
plus = []
minus = []
for b in books:
    if b>0:
        plus.append(b)
    else:
        minus.append(b)
plus.sort(reverse=True)
minus.sort()
ans = 0
p, m = 0, 0

moves = []
for i in range(0, len(plus), M):
    moves.append((plus[i], 1))
for i in range(0, len(minus), M):
    moves.append((minus[i], -1))
moves.sort(key=lambda x: abs(x[0]))
for a, b in moves:
    ans += a*b*2
ans -= moves[-1][0]*moves[-1][1]
print(ans)
