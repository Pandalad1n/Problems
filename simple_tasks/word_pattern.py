class Solution:
    def wordPattern(self, pattern, str):

        word_patterns = {}
        pattern_words = {}
        str = str.split(" ")

        if len(str) != len(pattern):
            return False

        for i, word in enumerate(str):
                word_patterns[pattern[i]] = word
                pattern_words[word] = pattern[i]

        for i, word in enumerate(str):
                if word_patterns[pattern[i]] != word:
                    return False
                if pattern_words[word] != pattern[i]:
                    return False

        return True

print(Solution().wordPattern("abba", "dog dog dog dog"))