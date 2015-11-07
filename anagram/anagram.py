def detect_anagrams(word, candidates):
    return [anagram for anagram in candidates
        if sorted(anagram.lower()) == sorted(word.lower()) and
        anagram.lower() != word.lower()]
