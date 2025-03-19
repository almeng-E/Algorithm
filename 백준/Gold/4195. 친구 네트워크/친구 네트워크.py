import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def make_set(n):
    p = [i for i in range(n+1)]
    return p

def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]

def union_set(a, b):
    r_a = find_parent(a)
    r_b = find_parent(b)
    if r_a == r_b:
        return
    else:
        p[r_a] = r_b
        size[r_b] += size[r_a]

def add_name(name):
    global idx
    if name not in name_idx:
        name_idx[name] = idx
        idx += 1

T = int(input())
for _ in range(T):
    F = int(input())

    p = make_set(2*F)
    size = [1] * (2 * F + 1)
    idx = 1
    name_idx = dict() # 이름 : idx

    for _ in range(F):
        a, b = input().split()
        # 이름 있는지 체크하고 추가
        add_name(a)
        add_name(b)
        a_idx = name_idx[a]
        b_idx = name_idx[b]

        union_set(a_idx, b_idx)

        print(size[find_parent(a_idx)])