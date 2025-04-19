word = input()
N = len(word)
w_list = []
for l in range(1, N-2):
    for r in range(l+1, N):
        w_list.append(word[:l][::-1] + word[l:r][::-1] + word[r:][::-1])


w_list.sort()
print(w_list[0])