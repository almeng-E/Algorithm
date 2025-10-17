from collections import deque
import sys
input = sys.stdin.readline
s = []
N = int(input())
q = deque(map(int, input().split()))


for nxt in range(1, N+1):
    if q and q[0] == nxt:
        q.popleft()
        continue
    if s and s[-1] == nxt:
        s.pop()
        continue
    p = 0
    while q:
        if q[0] != nxt:
            s.append(q.popleft())
        else:
            p = q.popleft()
            break
    if p:
        continue
    if s and s[-1] == nxt:
        s.pop()
        continue

    print('Sad')
    break
else:
    print('Nice')