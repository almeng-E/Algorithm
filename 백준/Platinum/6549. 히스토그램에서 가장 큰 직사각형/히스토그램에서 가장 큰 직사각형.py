import sys
input = sys.stdin.readline

while True:
    inp = list(map(int, input().split()))
    N = inp[0]
    if N == 0:
        break
    heights = inp[1:]
    heights.append(0)
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            max_area = max(max_area, width * height)
        stack.append(i)
    print(max_area)
