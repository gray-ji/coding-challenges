def solution(n, words):
    last_alphabet = words[0][0]
    used_words = set()

    for i, word in enumerate(words):
        if last_alphabet != word[0] or word in used_words:
            return [i%n + 1, i//n + 1]
        last_alphabet = word[-1]
        used_words.add(word)
    return [0, 0]