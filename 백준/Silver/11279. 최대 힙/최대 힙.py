import heapq
import sys
h=[]
def command(n,h):
    if n==0:
        if len(h)==0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -n)

n=int(sys.stdin.readline().rstrip())

for i in range(n):
    command(int(sys.stdin.readline().rstrip()), h)
    
