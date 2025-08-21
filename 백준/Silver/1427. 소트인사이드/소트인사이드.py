import sys
li=[]

for i in sys.stdin.readline().strip():
    li.append(i)
li.sort(reverse=True)
word=""
for j in li:
    word= word+j
print(word)