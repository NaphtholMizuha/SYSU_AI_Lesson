import queue
from typing import Tuple

from disjoint_set import *


def dijkstra(vertices: List[str], edges: List[Tuple[str, str, int]], start: str, end: str) -> Tuple[List[str], int]:
    dist = dict()
    dj = DisjointSet(vertices)  # get a disjoint set from the vertices
    for item in vertices:
        dist[item] = -1

    dist[start] = 0
    finished = False
    while not finished:
        q = queue.PriorityQueue()
        for edge in edges:
            (u, v, weight) = edge  # u and v are two ends of the edge and u is considered while v isn't
            if dj.is_linked(start, u) and not dj.is_linked(start, v) and (dist[v] == -1 or dist[u] + weight < dist[v]):
                q.put((weight, edge))

        if not q.empty():  # get the shortest edge in considered edges
            (u, v, weight) = q.get()[1]
            dist[v] = dist[u] + weight
            dj.union(u, v)

        finished = True

        for vertex in vertices:  # test whether all vertices are visited
            if not dj.is_linked(start, vertex):
                finished = False
    return dj.path(start, end), dist[end]
