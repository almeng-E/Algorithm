import sys
input = sys.stdin.readline


class Node:
    def __init__(self):
        self.children = dict()
        self.isTerminal = False


def dfs(node, depth):
    global res

    while len(node.children) == 1 and not node.isTerminal:
        k = list(node.children.keys())[0]
        node = node.children[k]

    if node.isTerminal:
        res += depth

    for ch in node.children.keys():
        nxt = node.children[ch]
        dfs(nxt, depth+1)

while True:
    try:
        ROOT = Node()
        # 트라이 구성
        N = int(input())
        for _ in range(N):
            S = input().rstrip()
            CUR = ROOT
            for ch in S:
                if ch not in CUR.children:
                    nxt = Node()
                    CUR.children[ch] = nxt

                CUR = CUR.children[ch]
            CUR.isTerminal = True






        # DFS
        res = 0
        for inp in ROOT.children.keys():
            dfs(ROOT.children[inp], 1)

        print(f"{round(res/N, 2):.2f}")


    except:
        break