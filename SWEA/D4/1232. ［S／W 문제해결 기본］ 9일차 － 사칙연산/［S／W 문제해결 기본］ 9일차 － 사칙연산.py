# Node 클래스 연습 저장용
class Node:
    def __init__(self, data, left_node_num, right_node_num):
        self.data = data
        self.left_node_num = left_node_num
        self.right_node_num = right_node_num


def post_order(v):
    global res

    # 숫자임
    if tree[v].left_node_num is None:
        return tree[v].data


    # 연산자일 경우 순회
    # 좌
    a = post_order(tree[v].left_node_num)
    # 우
    b = post_order(tree[v].right_node_num)
    # 연산자
    c = tree[v].data
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a/b


for TC in range(10):
    N = int(input())

    tree = dict()

    # 정점 정보 입력
    for _ in range(N):
        li = input().split()
        if li[1].isdigit():
            tree[int(li[0])] = Node(float(li[1]), None, None)
        else:
            tree[int(li[0])] = Node(li[1], int(li[2]), int(li[3]))


    # 후위 순회
    res = post_order(1)
    print(f'#{TC+1} {int(res)}')