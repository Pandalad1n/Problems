class Solution:
    def maxArea(self, height):
        max_val = 0
        i = 0
        j = len(height) - 1
        while i != j:
            max_val = max(max_val, min(height[i], height[j]) * (j - i))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return max_val

print(Solution().maxArea(([2,1])))