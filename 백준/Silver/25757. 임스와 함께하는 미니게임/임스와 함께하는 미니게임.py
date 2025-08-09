import sys
input = sys.stdin.readline

N, G = input().split()

if G == "Y":
    M = 1
elif G == 'F':
    M = 2
else :
    M = 3

played = set()
cnt = 0

for _ in range(int(N)):
    p = input().rstrip()
    if p not in played:
        played.add(p)
        cnt += 1
print(cnt//M)




