class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i_s = i_p = 0
        while i_p < len(p) and i_s < len(s):
            next_ast = i_p + 1 < len(p) and p[i_p + 1] == "*"
            matches = s[i_s] == p[i_p] or p[i_p] == "."

            if next_ast:
                if self.isMatch(s[i_s:], p[i_p + 2:]):
                    return True

                if matches:
                    i_s += 1
                    continue

                i_p += 2

            if not matches:
                return False

            i_s += 1
            i_p += 1

        if i_p + 1 < len(p) and p[i_p + 1] == "*":
            if self.isMatch(s[i_s:], p[i_p + 2:]):
                return True

        if i_s < len(s) or i_p < len(p):
            return False

        return True


cases = (
    ("abba", "...."),
    ("abba", ".sd."),
    ("abba", "ab.a*"),
    ("abba", "...."),
    ("abba", "abc*ba"),
    ("abba", "abb*a*v*n*a"),
    ("abba", ".*"),
    ("abba", "abba.*"),
    ("abba", "a.*"),
    ("aa", "a*"),
    ("mississippi", "mis*is*p*."),
    ("ab", ".*c"),
    ("aaa", "a*a"),
    ("a", ".*.."),
    ("a", "ab*"),
)

for c in cases:
    print(c, Solution().isMatch(c[0], c[1]))
