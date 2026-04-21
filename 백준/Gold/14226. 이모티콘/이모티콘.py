import sys
input = sys.stdin.readline

from collections import deque


def paste(cur, t, clip):
    nxt = cur+clip
    if nxt <= 2000 and v[nxt][clip] > t+1:
        v[nxt][clip] = t+1
        q.append((nxt, t+1, clip))


def copy(cur, t, clip):
    n_clip = cur
    if n_clip <= 1000 and v[cur][n_clip] > t+1:
        v[cur][n_clip] = t+1
        q.append((cur, t+1, n_clip))


def delete(cur, t, clip):
    nxt = cur-1
    if nxt >= 0 and v[nxt][clip] > t+1:
        v[nxt][clip] = t+1
        q.append((nxt, t+1, clip))


S = int(input())
# v[개수][클립보드] = 시간
v = [[float('inf') for _ in range(2001)] for _ in range(2001)]

q = deque()
q.append((1, 0, 0))
v[1][0] = 0


while q:
    cur, t, clip = q.popleft()
    if cur == S:
        print(t)
        break

    paste(cur, t, clip)
    copy(cur, t, clip)
    delete(cur, t, clip)

