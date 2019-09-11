import statistics


class Solution:
    def splitArraySameAverage(self, A):
        pivot_avg = statistics.mean(A)
        for prev in self.reccuravg(A, pivot_avg, len(A)):
            for i in range(len(A)):
                avg = (prev + A[i]) / 2
                if avg > pivot_avg:
                    return False
                if avg == pivot_avg:
                    return True

        return False

    def reccuravg(self, A, pivot_avg, until):
        if until == 0:
            return

        for prev in self.reccuravg(A, pivot_avg, until - 1):
            for i in range(until):
                avg = (prev + A[i]) / 2
                if avg > pivot_avg:
                    return

                yield avg


print(Solution().splitArraySameAverage([1,2,3,4,5,6,7,8]))
# print(Solution().splitArraySameAverage([0, 16]))