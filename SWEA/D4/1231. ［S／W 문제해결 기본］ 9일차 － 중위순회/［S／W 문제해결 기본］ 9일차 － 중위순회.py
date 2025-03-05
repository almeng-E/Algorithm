def in_order(v):
    if v not in tree:
        return

    if tree[v][1]:
        in_order(tree[v][1][0])
    print(tree[v][0], end="")
    if len(tree[v][1]) == 2:
        in_order(tree[v][1][1])




for TC in range(10):
    N = int(input())

    tree = dict()

    # 정점 정보 입력
    for _ in range(N):
        a, b, *c = input().split()
        tree[int(a)] = (b, list(map(int, c)))


    print(f'#{TC+1} ', end="")
    in_order(1)
    print()