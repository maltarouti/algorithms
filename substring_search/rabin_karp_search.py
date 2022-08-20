
class RabinKarp:
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.alphabet_size = 26
        self.prime = 7

    def search(self):
        text_size = len(self.text)
        pattern_size = len(self.pattern)

        hash_text = 0
        hash_pattern = 0

        h = 1
        for _ in range(pattern_size-1):
            h = (h*self.alphabet_size) % self.prime

        for i in range(pattern_size):
            hash_pattern = (self.alphabet_size*hash_pattern +
                            ord(self.pattern[i])) % self.prime

            hash_text = (self.alphabet_size * hash_text +
                         ord(self.text[i])) % self.prime

        for i in range(text_size-pattern_size+1):

            if hash_text == hash_pattern:

                j = 0

                while j < pattern_size:
                    if self.text[i+j] != self.pattern[j]:
                        break

                    j = j + 1

                if j == pattern_size:
                    print("Found match at index %s" % i)

            if i < text_size-pattern_size:
                hash_text = ((hash_text - ord(self.text[i]) * h)
                             * self.alphabet_size
                             + ord(self.text[i + pattern_size])) % self.prime

                if hash_text < 0:
                    hash_text = hash_text + self.prime


if __name__ == "__main__":
    algorithm = RabinKarp("Birds are so cute", "cute")
    algorithm.search()
