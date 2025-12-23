import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    q = deque()
    for i in range(N):
        q.append((i+1, arr[i]))
    
    ret = []
    for _ in range(N-1):
        cur, move = q.popleft()
        ret.append(cur)
        if move > 0:
            for _ in range(move-1):
                q.append(q.popleft())
        else:
            for _ in range(-move):
                q.appendleft(q.pop())
    ret.append(q[0][0])
    print(*ret)
solve()