while True:
    sentence = input().rstrip()

    if sentence == '.':
        break

    stack = []
    for i in sentence:
        if i in ('(', '['):
            stack.append(i)
        elif i == ')':
            try:
                a = stack.pop()
                if a == '(':
                    continue
                else:
                    print('no')
                    break
            except IndexError:
                print('no')
                break
        elif i == ']':
            try:
                a = stack.pop()
                if a == '[':
                    continue
                else:
                    print('no')
                    break
            except IndexError:
                print('no')
                break
        else:
            continue
    else:
        if stack:
            print('no')
        else:
            print('yes')