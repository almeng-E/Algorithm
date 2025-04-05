import sys
input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

G = int(input())
B = int(input())

p = [i for i in range(G+1)]

res = 0
for _ in range(B):
    i = int(input())
    if p[find(i)]:
        res += 1
        p[find(i)] -= 1
        find(i)
    else:
        break

print(res)