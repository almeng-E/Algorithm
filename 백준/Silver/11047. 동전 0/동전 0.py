import sys

n,k=map(int,sys.stdin.readline().split())
coins=[int(sys.stdin.readline().rstrip()) for _ in range(n)]

cnt=0

while k>0:
    a=coins.pop()
    cnt+= k//a
    k= k%a
    
print(cnt)