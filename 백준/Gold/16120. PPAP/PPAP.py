import sys
input = sys.stdin.readline

S = input().rstrip()
st = []
for c in S:
    st.append(c)
    if c == 'P':
        if len(st) >= 4 and ''.join(st[-4:]) == 'PPAP':
            for _ in range(4):
                st.pop()
            st.append(c)
print('PPAP' if (len(st)==1 and st[0]=='P') else 'NP')
