def switch_card(depth):
    global res
    if depth == change:
        res = max(res, int("".join(cards)))
        return

    # 교환 후보 만들기
    for i in range(len(cards)-1):
        for j in range(i+1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]
            arr = ''.join(cards)
            if (depth, arr) not in memo:
                memo.append((depth, arr))
                switch_card(depth+1)
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for TC in range(T):

    cards, change = input().split()
    change = int(change)
    cards = list(cards)

    memo = []
    res = 0
    switch_card(0)
    print(f'#{TC+1} {res}')