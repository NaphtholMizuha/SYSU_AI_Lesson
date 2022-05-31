import typing
from typing import *
from parse import *

def read_file(path: AnyStr) -> List[AnyStr]:
    file = open(path, 'r')
    ipt = file.read()
    strs = ipt.split('\n')
    return strs

if __name__ == '__main__':
    clause_set = parse_clause_set(read_file('src.txt'))
    print(clause_set)
    clause_set.reasoning()
    print("Hello, world!")
