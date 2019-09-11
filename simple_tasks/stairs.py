class Solution:
    def arrangeCoins(self, n: int) -> int:
        stairs = 0
        i = 1
        while True:
            if n - i < 0:
                break
            n -= i
            i += 1
            stairs += 1
        return stairs

print(Solution().arrangeCoins(1))