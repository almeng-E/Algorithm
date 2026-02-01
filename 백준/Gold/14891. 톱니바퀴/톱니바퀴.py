import sys
input = sys.stdin.readline

# 비트마스킹, 비트쉬프트 연습하자..

def rotate(g_id, direction):
    global G
    if direction == 0:
        return
    elif direction == 1:
        tmp = G[g_id] & 1
        G[g_id] >>= 1
        if tmp:
            G[g_id] |= (1 << 7)
    else:
        tmp = G[g_id] & (1 << 7)
        G[g_id] <<= 1
        G[g_id] &= 0xFF
        if tmp:
            G[g_id] |= 1


G = [0] * 4
for i in range(4):
    g = input().rstrip()
    for j in range(8):
        if g[j] == '1':
            G[i] |= (1 << (8-j-1))


for _ in range(int(input())):
    g_id, direction = map(int, input().split())
    g_id -= 1
    dirs = [0, 0, 0, 0]
    dirs[g_id] = direction

    for i in range(g_id+1, 4):
        if bool(G[i] & (1 << 1)) == bool(G[i-1] & (1 << 5)):
            break
        else:
            dirs[i] = -dirs[i-1]

    for i in range(g_id-1, -1, -1):
        if bool(G[i] & (1 << 5)) == bool(G[i+1] & (1 << 1)):
            break
        else:
            dirs[i] = -dirs[i+1]

    for i in range(4):
        rotate(i, dirs[i])

    ans = 0
    for i in range(4):
        if G[i] & (1 << 7):
            ans |= (1 << i)
print(ans)


