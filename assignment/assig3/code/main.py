from bfs import *
from ids import *
from time import process_time

if __name__ == '__main__':
    file = open('result.txt', 'w')
    m = read_maze('MazeData.txt')
    bfs_start = process_time()
    bfs_res = bfs(m)
    bfs_end = process_time()
    file.write('BFS:\n' + str(get_list(bfs_res, m.end)) + '\n' + f'takes {bfs_end - bfs_start} secs\n\n')

    ids_start = process_time()
    ids_res, depth = ids(m)
    ids_end = process_time()

    if ids_res is None:
        file.write("Not found\n")
    else:
        file.write('IDS:\n' + str(get_list(ids_res, m.end)) + '\n' + f'takes {ids_end - ids_start} secs\n')
        file.write(f'at depth {depth}\n')

