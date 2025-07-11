N, X = map(int, input().split())
arr = [0] + list(map(int, input().split()))

m_v = 0
m_cnt = 0

w = sum(arr[:X])

for i in range(X, N+1):
    w -= arr[i-X]
    w += arr[i]

    if m_v < w:
        m_v = w
        m_cnt = 1
    elif m_v == w:
        m_cnt += 1


if m_v == 0:
    print('SAD')
else:
    print(m_v)
    print(m_cnt)