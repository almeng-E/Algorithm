N = int(input())
di = dict()

calc = input()

for i in range(65, 65+N):
    di[chr(i)] = float(input())

stack = []

for i in calc:
    if i in di:
        stack.append(di[i])
    else:
        a, b = stack.pop(), stack.pop()
        if i == '*':
            stack.append(a*b)
        elif i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(b-a)
        elif i == '/':
            stack.append(b/a)

print(f'{stack[0]:.2f}')