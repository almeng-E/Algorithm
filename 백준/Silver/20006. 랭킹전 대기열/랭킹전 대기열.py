import sys
input = sys.stdin.readline
p, m = map(int, input().split())

rooms = [[] for _ in range(p)]
nxt_room = 0

for _ in range(p):
    player = input().split()

    for i in range(nxt_room):
        if len(rooms[i]) >= m:
            continue
        if abs(int(rooms[i][0][0]) - int(player[0])) > 10:
            continue
        rooms[i].append(player)
        break
    else:
        rooms[nxt_room].append(player)
        nxt_room += 1

for i in range(nxt_room):
    room = rooms[i]

    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')

    for p in sorted(room, key= lambda x: x[1]):
        print(*p)