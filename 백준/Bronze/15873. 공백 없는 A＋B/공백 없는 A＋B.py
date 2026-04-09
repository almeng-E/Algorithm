import sys;input=sys.stdin.readline;
S = input().rstrip()
if len(S)==2:
    print(int(S[0])+int(S[1]))
elif len(S)==3:
    if S[1]=='0':
        print(int(S[:2])+int(S[2]))
    else:
        print(int(S[0])+int(S[1:]))
else:
    print(int(S[:2])+int(S[2:]))