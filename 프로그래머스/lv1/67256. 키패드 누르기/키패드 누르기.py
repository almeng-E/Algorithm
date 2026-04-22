def solution(numbers, hand):
    def move_left():
        nonlocal lx, ly, tx, ty
        answer.append('L')
        lx, ly = tx, ty
        
    def move_right():
        nonlocal rx, ry, tx, ty
        answer.append('R')
        rx, ry = tx, ty
    
    answer = []
    pad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1),
    }
    
    lx, ly = 3, 0
    rx, ry = 3, 2
    
    L = {1, 4, 7}
    R = {3, 6, 9}
    
    for num in numbers:
        tx, ty = pad[num]

        if num in L:
            move_left()
            continue
        if num in R:
            move_right()    
            continue
        
        ld = abs(tx-lx) + abs(ty-ly)
        rd = abs(tx-rx) + abs(ty-ry)
        if ld < rd:
            move_left()
        elif ld > rd:
            move_right()   
        else:
            if hand == 'left':
                move_left()
            else:
                move_right()
    
    return ''.join(answer)