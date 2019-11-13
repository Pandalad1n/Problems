class Solution:
    def minFlipsMonoIncr(self, s):
        zero, one = 0, 0
        for c in s:
            if c == "0":
                zero += 1

        ans = zero

        for c in s:
            if c == "0":
                zero -= 1
            else:
                one += 1

            print(ans, zero + one)
            ans = min(ans, zero + one)

        return ans


print(Solution().minFlipsMonoIncr("10011111110010111011"))
