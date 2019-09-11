class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            tail, head = i+1, len(nums) - 1
            while tail < head:
                guess = nums[i] + nums[tail] + nums[head]
                if guess < target:
                    tail += 1
                if guess > target:
                    head -= 1
                if guess == target:
                    closest = guess
                    break
                if abs(guess - target) < abs(closest - target):
                    closest = guess

        return closest

print(Solution().threeSumClosest([0,1,2], 3))