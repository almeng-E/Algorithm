import sys
input = sys.stdin.readline
from collections import deque

def main():
    N, K = map(int, input().split())
    D = deque(map(int, input().split()))
    Z = 0
    for i in D:
        if i == 0:
            Z += 1
    LEN = 2*N
    Q = deque([0] * LEN)
    ans = 0
    while Z < K:
        ans += 1
        # 1:
        D.rotate()
        Q.rotate()
        Q[N-1] = 0
    
        # 2:
        for i in range(N-2, -1, -1):
            if Q[i] and not Q[i+1] and D[i+1]:
                Q[i+1] = Q[i]
                Q[i] = 0
                D[i+1] -= 1
                if D[i+1] == 0:
                    Z += 1
        Q[N-1] = 0
    
        # 3:
        if D[0]:
            D[0] -= 1
            Q[0] = 1
            if D[0] == 0:
                Z += 1
    
    print(ans)
main()