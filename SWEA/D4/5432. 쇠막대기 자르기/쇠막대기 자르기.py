T = int(input())
for TC in range(T):

    stack = 1
    result = 0
    word = input()
    for i in range(1, len(word)):
        if word[i] == '(':
            stack += 1
        if word[i] == ')':
            if word[i-1] == '(':
                stack -= 1
                result += stack
            else:
                stack -= 1
                result += 1
    print(f'#{TC+1} {result}')