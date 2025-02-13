for TC in range(10):
    n, word = input().split()
    stack = []


    for i in word:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{TC+1}', ''.join(stack))

