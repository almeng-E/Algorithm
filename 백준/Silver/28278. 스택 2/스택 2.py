import sys
input = sys.stdin.readline

stack = []

N = int(input())
for _ in range(N):
    a, *b = map(int, input().split())
    if a == 1:
        stack.append(b[0])
    elif a == 2:
        print(stack.pop() if stack else -1)
    elif a == 3:
        print(len(stack))
    elif a == 4:
        print(1 if not stack else 0)
    elif a == 5:
        print(stack[-1] if stack else -1)