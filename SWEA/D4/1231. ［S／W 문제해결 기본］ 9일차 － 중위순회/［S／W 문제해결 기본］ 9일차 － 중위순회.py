# Node 클래스 연습 저장용
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node



def in_order(node):
    if node == 0:
        return

    in_order(tree[node].left_node)
    print(tree[node].data, end="")
    in_order(tree[node].right_node)




for TC in range(10):
    N = int(input())

    tree = dict()

    # 정점 정보 입력
    for _ in range(N):
        a, b, *c = input().split()
        if len(c) == 0:
            c = [0, 0]
        elif len(c) == 1:
            c.append(0)
        tree[int(a)] = Node(b, int(c[0]), int(c[1]))

    print(f'#{TC+1} ', end="")
    in_order(1)
    print()