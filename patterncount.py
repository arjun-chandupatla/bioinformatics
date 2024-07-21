def pattern_count(text: str, pattern: str) -> int:
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        text[i:i+len(pattern)]
        if text[i:i+len(pattern)] == pattern:
            print(text[i:i+len(pattern)])
            count += 1
    return count


print(pattern_count("gcgcg", "gcg"))