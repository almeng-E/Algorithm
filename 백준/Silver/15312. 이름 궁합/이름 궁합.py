import sys
input = sys.stdin.readline

vals = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A = input().rstrip()
B = input().rstrip()

queue = []
for i in range(len(A)):
    queue.append(vals[ord(A[i])-65])
    queue.append(vals[ord(B[i])-65])

while len(queue) > 2:
    n_queue = []
    for i in range(len(queue)-1):
        n_queue.append((queue[i] + queue[i+1])%10)
    queue = n_queue

print(f'{queue[0]}{queue[1]}')