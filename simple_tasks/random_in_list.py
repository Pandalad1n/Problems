from array import array
import random


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        index_list = []
        for i, n in enumerate(self.nums):
            if n == target:
                index_list.append(i)
        return random.choice(index_list)


print(Solution([1,2,3]).pick(2))