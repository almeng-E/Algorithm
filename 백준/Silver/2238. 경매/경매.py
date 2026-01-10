import sys
input = sys.stdin.readline

U, N = map(int, input().split())
bid = [[] for _ in range(U+1)]
for _ in range(N):
    S, P = input().split()
    bid[int(P)].append(S)
cost, cnt = 0, float('inf')
for i in range(1, U+1):
    if not bid[i]:
        continue
    if len(bid[i]) < cnt:
        cnt = len(bid[i])
        cost = i
print(bid[cost][0], cost)