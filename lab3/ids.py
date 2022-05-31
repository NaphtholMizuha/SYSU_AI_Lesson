from Maze import *
from collections import deque

def ids(m: Maze):
    global file 
    file = open('ids.txt', 'w')
    for depth in range(100):
        res = dls(m, depth)
        if res is None:
            continue
        else:
            file.close()
            return res, depth
    file.close()
    return None


def dls(m: Maze, max_depth: int):
    stack = deque()
    closed = []  # store the points expanded
    stack.append(m.start)
    precursor = {m.start: m.start}
    depth = {m.start: 0}
    

    while not len(stack) == 0:
        top = stack.pop()
        closed.append(top)
        for adj_state in adj(top):
            if m.is_valid(adj_state) and closed.count(adj_state) == 0 and depth[top] <= max_depth:
                stack.append(adj_state)
                closed.append(adj_state)
                depth[adj_state] = depth[top] + 1
                precursor[adj_state] = top
                file.write(str(len(stack)) + '\n')
                if adj_state == m.end:
                    file.close()
                    return precursor
    
    return None