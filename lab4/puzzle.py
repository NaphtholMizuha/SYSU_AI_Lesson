from typing import Tuple

PuzzleLine = Tuple[int, int, int, int]
Puzzle = Tuple[PuzzleLine, PuzzleLine, PuzzleLine, PuzzleLine]

def puzzle2str(puzzle: Puzzle):
    print_str = ""
    for i in range(4):
        for j in range(4):
            print_str += f'{puzzle[i][j] if puzzle[i][j] != 0 else "":>2} '
        print_str += '\n'
    return print_str

def extensions(puzzle: Puzzle):
    result = []
    zero = (0, 0)
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 0:
                zero = (i, j)


    directions = [(0, 0, -1, 0), (0, 3, 1, 0), (1, 0, 0, -1), (1, 3, 0, 1)]
    for axid, bound, downward, rightward in directions:
        if zero[axid] != bound:
            row, col = zero
            temp = puzzle[row + downward][col + rightward]
            new_puzzle = []
            for i in range(4):
                new_puzzle_row = []
                for j in range(4):
                    if (i, j) == (row, col):
                        new_puzzle_row.append(temp)
                    elif (i, j) == (row + downward, col + rightward):
                        new_puzzle_row.append(0)
                    else:
                        new_puzzle_row.append(puzzle[i][j])
                new_puzzle.append(tuple(new_puzzle_row))

            result.append(tuple(new_puzzle))
    return result

def manhattan_dist(this: Puzzle, that: Puzzle):
    puzzle_dict_a = {}
    puzzle_dict_b = {}
    dist = 0
    for i in range(4):
        for j in range(4):
            puzzle_dict_a[this[i][j]] = (i, j)
            puzzle_dict_b[that[i][j]] = (i, j)

    for i in range(1, 16):
        a_x, a_y = puzzle_dict_a[i]
        b_x, b_y = puzzle_dict_b[i]
        dist += abs(a_x - b_x) + abs(a_y - b_y)

    return dist

def diff(this: Puzzle, that: Puzzle):
    count = 0
    for i in range(4):
        for j in range(4):
            if this[i][j] != that[i][j]:
                count += 1
    return count

def read(path, size): # calculate the same numbers distance in two puzzles
    file = open(path, 'r')
    lines = file.read().split('\n')
    a_str = lines[:size]
    b_str = lines[size + 1:]
    a = []
    b = []
    for line in a_str:
        strs = line.split(' ')
        nums = tuple([int(num) for num in strs])
        a.append(nums)

    for line in b_str:
        strs = line.split(' ')
        nums = tuple([int(num) for num in strs])
        b.append(nums)

    a = tuple(a)
    b = tuple(b)

    return a, b


