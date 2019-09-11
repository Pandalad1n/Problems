class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        count = 0
        customers_len = len(customers)

        for i, i_v in enumerate(customers):
            if grumpy[i] == 0:
                count += i_v
                customers[i] = 0

        cur_extra = sum(customers[:X])
        max_extra = cur_extra

        for i in range(X, customers_len):
            cur_extra = cur_extra - customers[i-X] + customers[i]
            max_extra = max(cur_extra, max_extra)

        count += max_extra
        return count



print(Solution().maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
