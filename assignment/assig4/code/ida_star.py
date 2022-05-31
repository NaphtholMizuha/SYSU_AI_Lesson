from puzzle import *

black = set()
path = []
count = 0

def ida_star(src: Puzzle, dest: Puzzle):
    global path
    global black
    bound = manhattan_dist(src, dest)
    path = [src]
    black = {src}

    while True:
        temp = ida_start_unit(dest, 0, bound)
        if temp == 0:
            print(f'IDA* algorithm completed which {count} states scanned, bound={bound}')
            return path
        elif temp == -1:
            return None
        bound = temp

def ida_start_unit(dest: Puzzle, depth: int, bound: int):
    global count
    count += 1
    target = path[-1] # stack `get`
    f = depth + manhattan_dist(target, dest)
    if f > bound:
        return f
    elif target == dest:
        return 0
    
    minimal = 99999999
    adj = extensions(target)
    for child in adj:
        if child in black:
            continue
        path.append(child)
        black.add(child)

        temp = ida_start_unit(dest, depth + 1, bound)
        if temp == 0:
            return 0
        elif temp < minimal:
            minimal = temp
        
        path.pop() # stack `pop`
        black.remove(child)

    return minimal
