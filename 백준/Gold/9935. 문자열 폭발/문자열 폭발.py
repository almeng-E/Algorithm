import sys
input = sys.stdin.readline
S = input().rstrip()
st = []
bomb = input().rstrip()
for c in S:
    st.append(c)
    if len(st) >= len(bomb) and ''.join(st[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            st.pop()
print(''.join(st) if st else 'FRULA')

