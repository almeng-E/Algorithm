import sys
from itertools import combinations

input=sys.stdin.readline

def distance(a,b):
    return (abs(a[0]-b[0])+abs(a[1]-b[1]))


n,m= map(int,input().split())

house=[]
chicken=[]
for i in range(n):
    tmpList=list(map(int,input().split()))
    for idx,val in enumerate(tmpList):
        if val==1:
            house.append((i+1,idx+1))
        elif val==2:
            chicken.append((i+1,idx+1))

result=987654321
for chi in combinations(chicken,m):
    tmp=0
    for h in house:
        chi_len=999
        for j in range(m):
            chi_len=min(chi_len, distance(h,chi[j]))
        tmp += chi_len
    result= min(result,tmp)
print(result)



