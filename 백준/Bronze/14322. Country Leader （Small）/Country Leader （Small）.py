T = int(input())
for tc in range(1, T+1):
    names = []
    N = int(input())
    for _ in range(N):
        s = input().rstrip()
        cnt = set()
        for c in s:
            if c == ' ':
                continue
            cnt.add(c)
        names.append((len(cnt), s))
    names.sort(key=lambda x: (-x[0], x[1]))
    print(f"Case #{tc}: {names[0][1]}")