from __future__ import annotations
from typing import List


class Vertex:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.visited: bool = False
        self.is_visiting: bool = False
        self.neighbors: list = []

    def add_neighbor(self, vertex: Vertex) -> None:
        self.neighbors.append(vertex)

    def __repr__(self) -> str:
        return self.name


class CycleDetection:
    def __init__(self, graph: List[Vertex]) -> None:
        self.graph = graph

    def detect_cycles(self) -> None:
        for vertex in self.graph:
            if not vertex.visited:
                self.dfs(vertex)

    def dfs(self, vertex: Vertex) -> None:
        vertex.is_visiting = True

        for v in vertex.neighbors:
            if v.is_visiting is True:
                print("There is a cycle in the given graph!")
                return

            if v.visited is not True:
                v.visited = True
                self.dfs(v)

        vertex.visited = True
        vertex.is_visiting = False


if __name__ == "__main__":
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    E = Vertex('E')
    F = Vertex('F')

    A.add_neighbor(C)
    A.add_neighbor(E)
    C.add_neighbor(B)
    C.add_neighbor(D)
    E.add_neighbor(F)
    F.add_neighbor(A)

    graph = [A, B, C, D, E, F]
    cycle_detection = CycleDetection(graph)
    cycle_detection.detect_cycles()
