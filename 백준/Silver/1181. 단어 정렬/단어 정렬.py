import sys
li=[]
for _ in range(int(sys.stdin.readline())):
    li.append(sys.stdin.readline().strip())
li=set(li)
li=list(li)

li.sort()
li.sort(key=len)

for i in li:
    print(i)