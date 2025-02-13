for TC in range(10):
    N = int(input())
    stack = []
    parens = input()
    for i in parens:
        if not stack:
            stack.append(i)
            continue
        if i in '([{<':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                break
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                break
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                break
        elif i == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                break
    if stack:
        print(f'#{TC+1} 0')
    else:
        print(f'#{TC+1} 1')