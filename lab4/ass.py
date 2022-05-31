def manhattan_dist(this, that):
    puzzle_dict_a = {}
    puzzle_dict_b = {}
    dist = 0
    for i in range(3):
        for j in range(3):
            puzzle_dict_a[this[i][j]] = (i, j)
            puzzle_dict_b[that[i][j]] = (i, j)

    for i in range(1, 9):
        a_x, a_y = puzzle_dict_a[i]
        b_x, b_y = puzzle_dict_b[i]
        dist += abs(a_x - b_x) + abs(a_y - b_y)

    return dist

if __name__ == '__main__':
    a = (
        (8, 1, 3),
        (7, 2, 4),
        (0, 6, 5),
    )

    b = (
        (1, 2, 3),
        (8, 0, 4),
        (7, 6, 5),
    )

    print(manhattan_dist(a, b))