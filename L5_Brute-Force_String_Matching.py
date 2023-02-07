def StringMatching(pattern, text):
    # pattern is a character array
    # text is a character array
    m = len(pattern)
    n = len(text)
    for i in range(0, n - m + 1): # i indexes text
        j = 0
        snapshot()
        while j < m and pattern[j] == text[i + j]:  # j indexes pattern
            j = j + 1
            snapshot()
        if j == m:
            snapshot()
            return i
    snapshot()
    return -1

clear_frames()
StringMatching("hello", "abchellodef")
show_animation(size=[10,7])