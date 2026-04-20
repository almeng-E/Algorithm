import sys
input = sys.stdin.readline


from collections import deque

N = int(input())
SCV = list(map(int, input().split()))
while len(SCV) < 3:
    SCV.append(0)
SCV.sort(reverse=True)
D = ((9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9))

v = [[[61 for _ in range(61)] for _ in range(61)] for _ in range(61)]
v[SCV[0]][SCV[1]][SCV[2]] = 0
q = deque()
q.append([0, *SCV])

while q:
    cnt, *cur = q.popleft()
    if cur[0]==0 and cur[1]==0 and cur[2]==0:
        break

    for d in D:
        nxt = cur[:]
        for i in range(3):
            nxt[i] = max(0, nxt[i]-d[i])
        if v[nxt[0]][nxt[1]][nxt[2]] > cnt+1:
            v[nxt[0]][nxt[1]][nxt[2]] = cnt+1
            q.append([cnt+1, *nxt])

print(v[0][0][0])
