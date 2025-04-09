N, M = map(int, input().split())

ms = list(map(int, input().split()))
cs = list(map(int, input().split()))

arr = list(zip(ms, cs))

# cost : value
MEMO = {}
MEMO[0] = 0

target = sum(ms)-M

for byte, cost in arr:
    # 현재 상태 메모
    tmp = {}
    for d_c, d_b in MEMO.items():
        # index-out
        if d_b + byte > target:
            continue

        if (d_c + cost) in MEMO:
            if MEMO[d_c + cost] <= d_b + byte:
                continue
        tmp[d_c + cost] = d_b + byte

    MEMO.update(tmp)

print(sum(cs) - max(MEMO.keys()))