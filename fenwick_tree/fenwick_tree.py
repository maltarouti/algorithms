from __future__ import annotations
from typing import List


class FenwickTree:
    def __init__(self, numbers: List[int]) -> None:
        self.numbers: List[int] = numbers
        self.fenwick_tree: List[int] = [0] * (len(numbers) + 1)

    def __next(self, index: int) -> int:
        return index + (index & -index)

    def __previous(self, index: int) -> int:
        return index - (index & -index)

    def __sum(self, index: int) -> int:
        index = index + 1
        total = 0

        while index:
            total = total + self.fenwick_tree[index]
            index = self.__previous(index)

        return total

    def range_sum(self, start: int, end: int) -> int:
        return self.__sum(end) - self.__sum(start-1)

    def construct(self) -> None:
        for index in range(1, len(self.numbers) + 1):
            self.update(index, self.numbers[index-1])

    def update(self, index: int, number: int) -> None:
        while index < len(self.numbers) + 1:
            self.fenwick_tree[index] += number
            index = self.__next(index)


if __name__ == "__main__":
    numbers = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]

    tree = FenwickTree(numbers)
    tree.construct()

    total = tree.range_sum(0, 6)
    print(f"The prefix sum is {total}")
