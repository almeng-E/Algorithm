import sys
input = sys.stdin.readline

# 라빈-카프 스러운 Rolling-hash
N, M = map(int, input().split())

base = 97
MOD = 10**9 + 9

inv_b = pow(base, MOD-2, MOD)


# 색상 입력 받기
colors = [set() for _ in range(2001)]
for _ in range(N):
    word = input().rstrip()
    val = 0
    L = len(word)
    for i in range(L):
        val *= base
        val += ord(word[i])
        val %= MOD
    colors[L].add(val)

# 이름 입력 받기
names = [set() for _ in range(2001)]
for _ in range(M):
    word = input().rstrip()
    val = 0
    L = len(word)
    # 거꾸로
    for i in range(L-1, -1, -1):
        val *= base
        val += ord(word[i])
        val %= MOD
    names[L].add(val)


# 검색하기
Q = int(input())
for _ in range(Q):
    word = input().rstrip()
    L = len(word)

    # 초기 해시 (\ /)
    right = 0
    for i in range(L-1, -1, -1):
        right *= base
        right += ord(word[i])
        right %= MOD

    left = 0
    ok = False

    # rolling - hash 접두 접미 검색
    for i in range(L-1):
        left *= base
        left += ord(word[i])
        left %= MOD

        right = ((right - ord(word[i]) + MOD) * inv_b) % MOD

        if left in colors[i+1] and right in names[L-i-1]:
            ok = True
            break

    print('Yes' if ok else 'No')