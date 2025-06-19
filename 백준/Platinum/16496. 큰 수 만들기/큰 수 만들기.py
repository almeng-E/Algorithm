import sys
input = sys.stdin.readline
N = int(input())
arr = input().split()
arr.sort(key=lambda x: x*10, reverse=True)
print(int(''.join(arr)))