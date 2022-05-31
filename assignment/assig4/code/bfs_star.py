from puzzle import *
from queue import PriorityQueue

def bfs_star(src: Puzzle, dest: Puzzle):
    prec = {src: None}
    count = 0
    depth = {src: 0} # g(x)
    weight = {src: manhattan_dist(src, dest)} # h(x)
    black = set()  # means "closed" list
    gray = PriorityQueue()
    gray.put((depth[src] + weight[src], src))
    

    while gray.qsize() > 0:
        target = gray.get()[1] # to get the minimal-weighted state to expand
        black.add(target)

        if target == dest: # to detect whether the destination was added
            print(f"A* algorithm completed with {count} states detected.")
            return prec

        for adj_puzzle in extensions(target):
            if adj_puzzle in black:
                continue

            depth[adj_puzzle] = depth[target] + 1
            weight[adj_puzzle] = manhattan_dist(adj_puzzle, dest)
            gray.put((depth[adj_puzzle] + weight[adj_puzzle], adj_puzzle))
            prec[adj_puzzle] = target
            count += 1





