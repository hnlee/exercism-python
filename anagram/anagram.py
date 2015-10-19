def detect_anagrams(word, candidates):
    return list(anagram for anagram in candidates
        if sorted(list(anagram.lower())) == sorted(list(word.lower())) and
        anagram.lower() != word.lower())
