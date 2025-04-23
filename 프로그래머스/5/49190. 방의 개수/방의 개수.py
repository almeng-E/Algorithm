def solution(arrows):
    answer = 0
    
    steps = ((-1, 0), (-1, +1), (0, +1), (+1, +1),
            (+1, 0), (+1, -1), (0, -1), (-1, -1))

    nodes = {
        (0, 0) : set()
    }
    x, y = 0, 0
    
    for d in arrows:
        for _ in range(2):
            nx, ny = x+steps[d][0], y+steps[d][1]
            if (nx, ny) in nodes:
                if d not in nodes[(nx, ny)]:
                    answer += 1
                nodes[(nx, ny)].add(d)
                nodes[(x, y)].add((d+4)%8)
            else:
                nodes[(nx, ny)] = {d}
                nodes[(x, y)].add((d+4)%8)
            x, y = nx, ny
    
    return answer