class Solution:
    def fourSum(self, nums, target):

        nums.sort()
        awns_nums = set()

        for j in range(len(nums)):
            for i in range(j + 1, len(nums)):
                tail, head = i+1, len(nums) - 1
                while tail < head:
                    guess = nums[i] + nums[j] + nums[tail] + nums[head]
                    if guess < target:
                        tail += 1
                    if guess > target:
                        head -= 1
                    if guess == target:
                        awns_nums.add((nums[i], nums[j], nums[tail], nums[head]))
                        tail += 1
                        head -= 1


        return awns_nums

print(Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0))