import sys
input = sys.stdin.readline

from heapq import heappop, heappush
T = int(input())
for _ in range(T):
    hi_q = []    # max-heap
    lo_q = []

    hi_lazy = [] # max-heap
    lo_lazy = []

    k = int(input())
    for _ in range(k):
        cmd, v = input().split()
        v = int(v)

        if cmd == 'I':
            heappush(hi_q, -v)
            heappush(lo_q, v)

        elif cmd == 'D':
            if v == 1:
                while hi_q and hi_lazy and hi_q[0] == hi_lazy[0]:
                    heappop(hi_q)
                    heappop(hi_lazy)
                if hi_q:
                    a = heappop(hi_q)
                    heappush(lo_lazy, -a)
            elif v == -1:
                while lo_q and lo_lazy and lo_q[0] == lo_lazy[0]:
                    heappop(lo_q)
                    heappop(lo_lazy)
                if lo_q:
                    a = heappop(lo_q)
                    heappush(hi_lazy, -a)

    while hi_q and hi_lazy and hi_q[0] == hi_lazy[0]:
        heappop(hi_q)
        heappop(hi_lazy)
    while lo_q and lo_lazy and lo_q[0] == lo_lazy[0]:
        heappop(lo_q)
        heappop(lo_lazy)

    if not hi_q:
        print('EMPTY')
    else:
        print(-hi_q[0], lo_q[0])