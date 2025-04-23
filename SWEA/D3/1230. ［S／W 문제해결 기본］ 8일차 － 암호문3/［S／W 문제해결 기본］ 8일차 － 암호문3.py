from collections import deque
for TC in range(10):
    N = int(input())
    pws = deque(input().split())
    M = int(input())
    commands = deque(input().split())

    while commands:
        C = commands.popleft()
        if C == 'I':
            x = int(commands.popleft())
            y = int(commands.popleft())
            s = []
            for _ in range(y):
                s.append(commands.popleft())
            for i in range(y-1, -1, -1):
                pws.insert(x, s[i])

        elif C == 'D':
            x = int(commands.popleft())
            y = int(commands.popleft())
            for _ in range(y):
                if pws[x]:
                    pws.remove(pws[x])
        else:
            y = int(commands.popleft())
            for _ in range(y):
                pws.append(commands.popleft())

    res = []
    for _ in range(10):
        res.append(pws.popleft())
    print(f'#{TC+1}', *res)