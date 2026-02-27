import sys
input = sys.stdin.readline
from heapq import heappop, heappush

Q = int(input())
ans = 0
gorilla = dict()

for _ in range(Q):
    cmd = input().split()
    name = cmd[1]
    if cmd[0] == '1':
        if name not in gorilla:
            gorilla[name] = []
        for i in map(int, cmd[3:]):
            heappush(gorilla[name], -i)
        
    else:
        b = int(cmd[2])
        if name not in gorilla:
            continue
        while gorilla[name] and b:
            i = heappop(gorilla[name])
            ans -= i
            b -= 1

print(ans)