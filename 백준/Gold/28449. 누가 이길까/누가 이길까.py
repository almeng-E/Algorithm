import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def solve():
    N, M = map(int, input().split())
    HI = list(map(int, input().split()))
    ARC = list(map(int, input().split()))
    
    HI.sort()
    ARC.sort()
    
    res = [0, 0, 0]
    
    for h in HI:
        l = bisect_left(ARC, h)
        r = bisect_right(ARC, h)
    
        res[0] += l
        res[2] += r-l
        res[1] += (M-r)
    
    print(*res)
solve()