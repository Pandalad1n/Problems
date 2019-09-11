class Solution:
    def merge(self, intervals):
        i = 0
        intervals.sort()

        def overlaps(it_1, it_2):
            if it_1[1] >= it_2[0]:
                return True

        def merge_its(it_1, it_2):
            return [min(it_1[0], it_2[0]), max(it_1[1], it_2[1])]

        if len(intervals) == 1:
            return intervals

        while i < len(intervals) - 1:
            if overlaps(intervals[i], intervals[i + 1]):
                intervals[i] = merge_its(intervals[i], intervals[i + 1])
                intervals.pop(i+1)
                i -= 1
            i += 1
        return intervals


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))