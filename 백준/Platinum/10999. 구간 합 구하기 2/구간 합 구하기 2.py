import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
lazy = [0] * SIZE

for i in range(N):
    tree[i + LEN] = int(input())

for i in range(LEN-1, 0, -1):
    tree[i] = tree[(i << 1)] + tree[(i << 1) + 1]


# lazy 처리 후 밀어내기
def push_down(node, s, e):
    '''
    node에 있던 lazy 값들 처리하고,
    있던 lazy 내려보내고
    lazy[node] = 0 처리해.
    '''
    # 할게 없네
    if lazy[node] == 0:
        return

    tree[node] += lazy[node] * (e - s + 1)

    # 리프노드면 내려보내면 안되지
    if s != e:
        lazy[(node << 1)] += lazy[node]
        lazy[(node << 1) + 1] += lazy[node]

    lazy[node] = 0


def range_update(node, s, e, ts, te, val):
    '''
    node 범위체크 등 하기 전에 lazy 있나 체크하고 내려보내기 ( == 최신 상태로 업데이트 하기 )
    범위 out -> X
    완전 포함 -> 최신 상태로 업데이트 하고, 자식은 lazy로 미루기
    더 들어가기 -> ... 재귀 호출 후 내 노드 최신화 (자식이 바뀌었을 수 있음)
    '''
    push_down(node, s, e)

    if te < s or e < ts:
        return

    if ts <= s and e <= te:
        tree[node] += val * (e - s + 1)
        if s == e:
            return
        lazy[(node << 1)] += val
        lazy[(node << 1) + 1] += val
        return

    mid = (s + e) // 2
    range_update((node << 1), s, mid, ts, te, val)
    range_update((node << 1) + 1, mid+1, e, ts, te, val)

    tree[node] = tree[(node << 1)] + tree[(node << 1) + 1]
    return


def range_get(node, s, e, ts, te):
    '''
    update랑 로직 비슷
    일단 lazy 있나 체크하고 내려보내고 (==최신 상태로 업데이트)
    범위 체크 and 재귀
    '''
    push_down(node, s, e)

    if te < s or e < ts:
        return 0

    if ts <= s and e <= te:
        return tree[node]

    mid = (s + e) // 2
    return range_get((node << 1), s, mid, ts, te) + range_get((node << 1) + 1, mid+1, e, ts, te)



for _ in range(M+K):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        _, b, c, d = cmd
        range_update(1, 0, LEN-1, b-1, c-1, d)


    elif cmd[0] == 2:
        _, b, c = cmd
        print(range_get(1, 0, LEN-1, b-1, c-1))
        