N, M = map(int, input().split())
schedule = [input().rstrip() for _ in range(N)]

for j in range(M):
    for i in range(N):
        if schedule[i][j] == 'O':
            break
    else:
        print(j+1)
        break
else:
    print('ESCAPE FAILED')