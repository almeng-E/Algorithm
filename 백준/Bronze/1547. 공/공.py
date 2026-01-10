import sys
input = sys.stdin.readline

cup = [0] * 4
cup[1] = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    cup[a], cup[b] = cup[b], cup[a]

for i in range(1, 4):
    if cup[i]:
        print(i)