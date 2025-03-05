def in_order(v):
    global c_index
    if v == 0 or v >= len(tree):
        return

    in_order(2*v)
    tree[v] = li[c_index]
    c_index += 1
    in_order(2*v + 1)


K = int(input())

li = list(map(int, input().split()))
c_index = 0

tree = [0] * (len(li) + 1)

in_order(1)

depth = 0
while depth < K:
    print(*tree[2**depth: 2**(depth+1)])
    depth += 1