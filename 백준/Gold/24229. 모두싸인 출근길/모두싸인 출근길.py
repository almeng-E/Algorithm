import sys
input = sys.stdin.readline

N = int(input())
w = [tuple(map(int, input().split())) for _ in range(N)]
w.append((float('inf'), float('inf')))
w.sort()

nw = []
jp = []
cl, cr = 0, 0
for i in range(N+1):
    l, r = w[i]
    if l <= cr:
        cr = max(cr, r)
    else:
        nw.append((cl, cr))
        jp.append(cr-cl)
        cl, cr = l, r
mr = [nw[i][1] for i in range(len(nw))]
for i in range(len(nw)-2, -1, -1):
    l, r, p = nw[i][0], nw[i][1], jp[i]
    for j in range(i+1, len(nw)):
        if nw[j][0] <= r + p:
            mr[i] = max(mr[i], mr[j])
        else:
            break
print(mr[0])