def solution(arrows):
    answer = 0
    
    steps = ((-1, 0), (-1, +1), (0, +1), (+1, +1),
            (+1, 0), (+1, -1), (0, -1), (-1, -1))

    nodes = {(0, 0), }
    edges = set() #(a,b == a->b)
    x, y = 0, 0
    
    for d in arrows:
        for _ in range(2):
            nx, ny = x+steps[d][0], y+steps[d][1]
            if (nx, ny) in nodes:
                if ((x, y), (nx, ny)) not in edges:
                    answer += 1

            nodes.add((nx, ny))
            edges.add(((x, y), (nx, ny)))
            edges.add(((nx, ny), (x, y)))

            x, y = nx, ny
    
    return answer