class Solution:
    def threeSum(self, nums):
        triplets = []
        for i_1 in range(len(nums)):
            for i_2 in range(i_1 + 1, len(nums)):
                for i_3 in range(i_2 + 1 , len(nums)):
                    a = 10
                    if nums[i_1] + nums[i_2] + nums[i_3] == 0 and sorted([nums[i_1], nums[i_2], nums[i_3]]) not in triplets:
                            triplets.append(sorted([nums[i_1], nums[i_2], nums[i_3]]))
        return triplets

    def threeSum_2(self, nums):
        res = set()
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return list(res)

print(Solution().threeSum_2([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))