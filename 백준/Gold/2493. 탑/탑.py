import sys
input = sys.stdin.readline

N = int(input())
tower = [float('inf')] + list(map(int, input().split()))


stack = [(tower[0], 0)]
res = []
for i in range(1, N+1):
    h = tower[i]
    while stack[-1][0] < h:
        stack.pop()

    res.append(stack[-1][1])
    stack.append((h, i))

print(*res)