class Solution:
  def isValid(self, s):
    counters = [0, 0, 0]
    for iter in s:
        btype = 0
        is_close = False
        if iter in ["{", "}"]:
            btype = 1
        if iter in ["[", "]"]:
            btype = 2
        if iter in [")", "}", "]"]:
            is_close = True

        if is_close:
            for i, c in enumerate(counters):
                if i == btype:
                    counters[btype] -= 1
                else:
                    counters[btype] -= c
        else:
            for i, c in enumerate(counters):
                if i == btype:
                    counters[btype] += 1
                else:
                    counters[btype] += c

        if counters[btype] < 0:
            return False

    for c in counters:
        if c != 0:
            return False

    return True


# Test Program
s = "{(([()()()()())])}"
# should return False
print(Solution().isValid(s))

s = "{()}"
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "(()([{]))}"
# should return False
print(Solution().isValid(s))
