class Solution:
    def largeGroupPositions(self, s):
        begin = 0
        awns = []
        i = 0

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                if i - begin >= 2:
                    awns.append([begin, i])
                begin = i + 1
            if i + 1 == len(s) - 1:
                if i + 1 - begin >= 2:
                    awns.append([begin, i + 1])

        return awns

print(Solution().largeGroupPositions("ggggggg"))