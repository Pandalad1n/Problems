class Solution:
    def longestCommonPrefix(self, strings):

        prefix = ''
        for chars in zip(*strings):
            print([char for char in chars])
            if not all(chars[0] == char for char in chars):
                break
            prefix += chars[0]
        return prefix


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))