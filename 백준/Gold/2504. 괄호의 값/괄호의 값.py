import sys
input = sys.stdin.readline

S = input().rstrip()

stack = []
tmp = 1
ans = 0

idx = 0
for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
        tmp *= 2
    elif S[i] == '[':
        stack.append('[')
        tmp *= 3

    elif S[i] == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break

        if S[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] != '[':
            ans = 0
            break
        if S[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

print(0 if stack else ans)
