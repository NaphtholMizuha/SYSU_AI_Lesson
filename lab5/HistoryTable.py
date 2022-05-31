import numpy as np

class HistoryTable:
    def __init__(self):
        self.table = {}

    def get(self, is_max, step):
        if self.table.get((is_max, step)) is None:
            return 0
        else:
            return self.table[(is_max, step)]

    def renew(self, is_max, step, depth):
        if self.table.get((is_max, step)) is None:
            self.table[(is_max, step)] = 2 << depth
        else:
            self.table[(is_max, step)] += 2 << depth