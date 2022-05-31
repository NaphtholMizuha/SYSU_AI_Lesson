from typing import *
Coordinate = Tuple[int, int]

def adj(c: Coordinate):
    return [(c[0] + 1, c[1]), (c[0], c[1] + 1), (c[0] - 1, c[1]), (c[0], c[1] - 1)]

def get_list(precursor: Mapping[Coordinate, Coordinate], end: Coordinate):
    x = end
    way = [x]
    while precursor[x] != x:
        x = precursor[x]
        way.append(x)
    way.reverse()
    return way

class Maze:
    def __init__(self, map: Mapping[Coordinate, bool], start: Coordinate, end: Coordinate, size: Coordinate):
        self.map = map
        self.start = start
        self.end = end
        self.length = size[0]
        self.width = size[1]

    def is_valid(self, c: Coordinate):
        x, y = c
        return 0 <= x < self.length and 0 <= y < self.width and self.map[(x, y)]


def read_maze(path: str):
    start = (0, 0)
    end = (0, 0)
    map = {}
    ipt = open(path).readlines()
    for i, line in enumerate(ipt):
        line = line[:-1]
        for j, char in enumerate(line):
            if char == '1':
                map[(i, j)] = False
            else:
                map[(i, j)] = True

            if char == 'S':
                start = (i, j)

            if char == 'E':
                end = (i, j)

    return Maze(map=map, start=start, end=end, size=(len(ipt), len(ipt[0]) - 1))