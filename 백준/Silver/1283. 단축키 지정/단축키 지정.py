import sys
input = sys.stdin.readline

N = int(input())
used = set()
for _ in range(N):
    found = False
    cmd = input().split()
    for i in range(len(cmd)):
        word = cmd[i]
        if not found and word[0].lower() not in used:
            used.add(word[0].lower())
            found = True
            cmd[i] = f'[{word[0]}]{word[1:]}'

    for i in range(len(cmd)):
        word = cmd[i]
        for j in range(len(word)):
            if not found and word[j].lower() not in used:
                used.add(word[j].lower())
                found = True
                cmd[i] = f'{word[0:j]}[{word[j]}]{word[j+1:]}'
    print(*cmd)