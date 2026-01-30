import sys
input = sys.stdin.readline

N = int(input())
arr = [0]
ans = [0] * (N+1)
v = [0] * (N+1)
for i in range(1, N+1):
    arr.append(int(input()))


for root in range(1, N+1):
    stack = []
    stack.append(root)
    is_cycle = True
    while True:
        nxt = arr[stack[-1]]
        if nxt == root:
            break
        if v[nxt]:
            is_cycle = False
            break
        v[nxt] = 1
        stack.append(nxt)

    if is_cycle:
        for i in stack:
            ans[i] = 1
            v[i] = 1
    else:
        for i in stack:
            v[i] = 0
print(sum(ans))
for i in range(N+1):
    if ans[i]:
        print(i)