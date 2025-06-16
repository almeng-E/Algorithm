import sys
input = sys.stdin.readline

from heapq import heappop, heappush, heapify

N, M = map(int, input().split())
cards = list(map(int, input().split()))
heapify(cards)

for _ in range(M):
    a = heappop(cards)
    b = heappop(cards)
    c = a+b
    heappush(cards, c)
    heappush(cards, c)
print(sum(cards))