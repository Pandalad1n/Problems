class Solution():
    def summaryRanges(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return str(nums[0])
        nums_li = []
        last = first = nums[0]
        nums = sorted(nums)

        for i in range(1, len(nums)):
            if nums[i] != last + 1:
                if last != first:
                    nums_li.append(str(first) + "-" + str(last))
                else:
                    nums_li.append(str(first))
                first = nums[i]
            last = nums[i]

            if i == len(nums) - 1:
                if last != first:
                    nums_li.append(str(first) + "-" + str(last))
                else:
                    nums_li.append(str(first))

        return ",".join(nums_li)

print(Solution().summaryRanges([1,5,3,2,4,11,88,9,10,8]))