from typing import List


class DisjointSet:
    def __init__(self, data: List[str]):
        self.fa = dict()  # “fa” means the precursor of the node
        for datum in data:
            self.fa[datum] = datum

    def find(self, x: str) -> str:  # find the ancestor of the node
        while self.fa[x] != x:
            x = self.fa[x]
        return x

    def union(self, x: str, y: str) -> None:  # union x and y, that is, make x be y's father
        self.fa[y] = x

    def is_linked(self, x: str, y: str) -> bool:  # judge whether x's ancestor is the same as y's
        return self.find(x) == self.find(y)

    def path(self, start: str, end: str) -> List[str]:  # make the shortest path from records of precursor of the
        # "end" node
        res = [end]
        while self.fa[end] != end:
            end = self.fa[end]
            res.append(end)

        res.reverse()
        if res[0] != start:  # that means "end" is unconnected with "start"
            return []
        else:
            return res
