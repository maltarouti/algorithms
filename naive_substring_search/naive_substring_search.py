

def naive_search(text: str, pattern: str) -> bool:
    text_size = len(text)
    pattern_size = len(pattern)

    for i in range(text_size - pattern_size + 1):
        j = 0

        while j < pattern_size:
            if text[i+j] != pattern[j]:
                break
            j += 1

        if j == pattern_size:
            return True
    return False


if __name__ == "__main__":
    text = "Birds are so cute!"
    pattern = "irds"
    print(naive_search(text, pattern))
