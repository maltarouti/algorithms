
class ZAlgorithm:

    def __init__(self, text: str, pattern: str) -> None:
        self.text = text
        self.pattern = pattern
        self.combination = pattern + text
        self.Z_table = [0] * len(self.combination)

    def construct_z_table(self) -> None:
        self.Z_table[0] = len(self.combination)
        left, right = 0, 0

        for k in range(1, len(self.combination)):
            if k > right:
                n = 0
                while (n+k < len(self.combination)
                       and self.combination[n] == self.combination[n+k]):

                    n = n + 1

                self.Z_table[k] = n

                if n > 0:
                    left = k
                    right = k + n - 1
            else:
                p = k - left
                if self.Z_table[p] < right - k + 1:
                    self.Z_table[k] = self.Z_table[p]
                else:
                    i = right + 1

                    while (i < len(self.combination)
                           and self.combination[i] == self.combination[i - k]):

                        i = i + 1

                    self.Z_table[k] = i - k
                    left = k
                    right = i - 1

    def search(self) -> None:
        self.construct_z_table()
        for i in range(1, len(self.Z_table)):
            if self.Z_table[i] >= len(self.pattern):
                index = i - len(self.pattern)
                print(f"Match found at index {index}")


if __name__ == "__main__":
    algorithm = ZAlgorithm('Birds are so cute!', 'irds')
    algorithm.search()
