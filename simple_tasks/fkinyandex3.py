class Solution():
    def summaryRanges(self, nums):
        nums = sorted(set(nums))
        print(nums)

        if not nums:
            return ""

        ranges = []
        prev = begin = nums[0]
        for i in nums:
            if i - prev > 1:
                if prev == begin:
                    ranges.append(str(prev))
                else:
                    ranges.append(str(begin) + "-" + str(prev))
                begin = i

            prev = i

        return ",".join(ranges)


print(Solution().summaryRanges([1,5,3,2,4,11, 143, 88,9,10,8]))