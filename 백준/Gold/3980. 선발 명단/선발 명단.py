def choose(depth, tmp):
    global res
    if depth == 11:
        res = max(res, tmp)
        return

    for p_num in range(11):
        if players[depth][p_num] != 0 and not picked_players[p_num]:
            picked_players[p_num] = True
            choose(depth+1, tmp + players[depth][p_num])
            picked_players[p_num] = False



C = int(input())
for _ in range(C):
    players = [list(map(int, input().split())) for _ in range(11)]

    players = list(zip(*players))

    picked_players = [False] * 11


    res = 0
    choose(0, 0)

    print(res)