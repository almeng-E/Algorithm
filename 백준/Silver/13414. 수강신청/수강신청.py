import sys
input = sys.stdin.readline

K, L = map(int, input().split())

d = dict()
cnt = 0
for _ in range(L):
    Sid = input().rstrip()
    cnt += 1
    d[Sid] = cnt

q = sorted(d.items(), key=lambda x: x[1])
K = min(K, len(q))
for i in range(K):
    print(q[i][0])