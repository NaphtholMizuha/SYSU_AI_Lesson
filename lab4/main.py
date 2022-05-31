from bfs_star import *
from ida_star import *
from puzzle import read
from time import process_time

def bfs_star_test(a, b):
    bfs_star_out = open('A*_output.txt', 'w')
    time_start = process_time()
    prec = bfs_star(a, b)
    time_end = process_time()
    print(f"It took {time_end - time_start} secs.")
    path = [b]
    while prec[b] is not None:
        b = prec[b]
        path.append(b)
    path.reverse()
    for i, state in enumerate(path):
        bfs_star_out.write(f'Move {i}:\n{puzzle2str(state)}\n')
    bfs_star_out.close()

def ida_star_test(a, b):
    ida_star_out = open('A*_output.txt', 'w')
    time_start = process_time()
    path = ida_star(a, b)
    time_end = process_time()
    print(f"It took {time_end - time_start} secs.")
    
    for i, state in enumerate(path):
        ida_star_out.write(f'Move {i}:\n{puzzle2str(state)}\n')
    ida_star_out.close()

if __name__ == '__main__':
    a, b = read('src.txt', 4)
    print(f"From:\n{puzzle2str(a)}\nTo:\n{puzzle2str(b)}")
    bfs_star_test(a, b)
    ida_star_test(a, b)
    
    
    
