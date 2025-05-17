level = 0
res = 0

cmd = input()
for i in range(len(cmd)):
    if cmd[i] == '(':
        level += 1
    else:
        if cmd[i-1] == '(':  # laser
            level -= 1
            res += level
        else:
            level -= 1
            res += 1
print(res)