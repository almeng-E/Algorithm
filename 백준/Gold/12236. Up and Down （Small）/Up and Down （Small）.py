import sys
input = sys.stdin.readline


def find_min(arr):
    m = float('inf')
    m_idx = 0
    for i in range(len(arr)):
        if m > arr[i]:
            m = arr[i]
            m_idx = i
    return m_idx


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        m_idx = find_min(A)
        lc = m_idx
        rc = len(A) - 1 - m_idx

        ans += min(lc, rc)
        A.pop(m_idx)
    print(f'Case #{tc}: {ans}')