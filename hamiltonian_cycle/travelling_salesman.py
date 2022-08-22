from __future__ import annotations
from typing import TypeVar

T = TypeVar("T")


class TravellingSalesman:
    def __init__(self, graph: list[list[int]]) -> None:
        self.graph = graph
        self.hamiltonian_cycles = []

        self.visited = [False] * len(self.graph)
        self.visited[0] = True
        self.path = [0] * len(self.graph)

    def is_valid(self, vertex: int, actual_position: int):
        if self.visited[vertex] or self.graph[actual_position][vertex] == 0:
            return False
        return True

    def tsp(self,
            actual_position: int,
            counter: int,
            cost: int):

        if counter == len(self.graph) and self.graph[actual_position][0]:
            self.path.append(0)
            print(self.path)
            self.hamiltonian_cycles.append(
                cost + self.graph[actual_position][0])
            self.path.pop()
            return

        for i, _ in enumerate(self.graph):
            if self.is_valid(i, actual_position):
                self.visited[i] = True
                self.path[counter] = i

                self.tsp(i, counter + 1, cost + self.graph[actual_position][i])
                self.visited[i] = False


if __name__ == '__main__':

    graph = [[0, 1, 0, 2, 0],
             [1, 0, 1, 0, 2],
             [0, 1, 0, 3, 1],
             [2, 0, 3, 0, 1],
             [0, 2, 1, 1, 0]]

    tsp = TravellingSalesman(graph)
    tsp.tsp(0, 1, 0)
    print("The cost of Hamiltonian Cycle is", min(tsp.hamiltonian_cycles))
