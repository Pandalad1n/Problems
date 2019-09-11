class Solution:
    def heightChecker(self, h):
        count = 0
        for i in range(len(h) - 1):
            if h[i] > h[i + 1]:
                count += 1
            elif h[i + 1] < h[i]:
                count += 1
        return count

print(Solution().heightChecker([1,1,4,2,1,3]))