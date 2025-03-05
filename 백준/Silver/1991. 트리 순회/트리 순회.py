import sys
input = sys.stdin.readline


def traversal(v, num):
    if v == '.':
        return
    if num == 1:
        print(tree[v].data, end="")
    traversal(tree[v].left_node, num)
    if num == 2:
        print(tree[v].data, end="")
    traversal(tree[v].right_node, num)
    if num == 3:
        print(tree[v].data, end="")


class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node



N = int(input())

tree = {}

# 트리 정보 입력
for _ in range(N):
    d, l, r = input().split()
    tree[d] = Node(d, l, r)

traversal('A', 1)
print()
traversal('A', 2)
print()
traversal('A', 3)