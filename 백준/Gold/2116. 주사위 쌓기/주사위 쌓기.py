import sys
input = sys.stdin.readline

# A-F / B-D / C-E

dice = []
N = int(input())
for _ in range(N):
    a, b, c, d, e, f = map(int, input().split())
    if a>f: a,f = f,a
    if b>d: b,d = d,b
    if c>e: c,e = e,c
    dice.append([[a, f], [b, d], [c, e]])
    dice[-1].sort()


ans = 0
for i in range(1, 7):
    bot = i
    p_id = 0
    tmp = 0
    for d in dice:
        cur_max = 0
        for j in range(3):
            x, y = d[j]
            if bot == x:
                bot = y
                p_id = j
                break
            if bot == y:
                bot = x
                p_id = j
                break
        for j in range(3):
            if j == p_id:
                continue
            cur_max = max(cur_max, d[j][1])
        tmp += cur_max
    ans = max(ans, tmp)
print(ans)