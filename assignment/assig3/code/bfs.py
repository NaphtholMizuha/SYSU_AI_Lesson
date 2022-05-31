from Maze import *
from collections import deque

def bfs(m: Maze):
    opening = deque() # store the points to be expanded
    closed = [] # store the points expanded
    opening.append(m.start) # the 1st point is the start point
    precursor = {m.start: m.start}
    file = open('bfs.txt', 'w')

    while True:
        front = opening.popleft()
        for target in adj(front):
            if m.is_valid(target) and closed.count(target) == 0:
                opening.append(target)
                file.write(str(len(opening)) + '\n')
                precursor[target] = front

        closed.append(front)
        if front == m.end:
            break
    file.close()
    return precursor