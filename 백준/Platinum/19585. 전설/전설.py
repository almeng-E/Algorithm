import sys
input = sys.stdin.readline
class Node:
    def __init__(self):
        self.is_terminal = False
        self.child = {}

C, N = map(int, input().split())

c_root = Node()

# color-trie
for _ in range(C):
    cur = c_root
    word = input().rstrip()
    for s in word:
        if s not in cur.child:
            cur.child[s] = Node()
        cur = cur.child[s]

    cur.is_terminal = True

names = set(input().rstrip() for _ in range(N))

# search
Q = int(input())
for _ in range(Q):
    res = False
    word = input().rstrip()
    cur = c_root
    found = False
    for i in range(len(word)):
        # color-trie 탐색
        if word[i] in cur.child:
            # 다음 노드가 있음
            cur = cur.child[word[i]]
        else:
            # 없음 => 색 오류
            break

        if cur.is_terminal:
            # 색의 후보 -> 이름 탐색
            if word[i+1:] in names:
                res = True
                break


    print('Yes' if res else 'No')