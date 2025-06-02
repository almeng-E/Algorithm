import sys
input = sys.stdin.readline


n, m = map(int, input().split())


res = 0
li = [0]

for i in map(int, input().split()):
    res += i
    li.append(res)

for _ in range(m):
    i, j = map(int, input().split())
    print(li[j]-li[i-1])