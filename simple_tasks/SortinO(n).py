import random

class Solution():
    def __init__(self, nums):
        self.nums = nums

    def swap(self, left, right):
        t = self.nums[left]
        self.nums[left] = self.nums[right]
        self.nums[right] = t

    def sortNums(self):
        last_i = len(self.nums)-1
        first_i = 0
        right_swap = last_i
        left_swap = first_i
        right_i = last_i
        left_i = first_i

        for _ in self.nums:
            if self.nums[right_i] > self.nums[last_i]:
                right_swap = last_i
            if self.nums[right_i] > self.nums[right_swap]:
                self.swap(right_i, right_swap)
            if self.nums[right_swap] == self.nums[last_i]:
                right_swap -= 1
            right_i -= 1

        for _ in self.nums:
            if self.nums[left_i] < self.nums[first_i]:
                left_swap = first_i
            if self.nums[left_i] < self.nums[left_swap]:
                self.swap(left_i, left_swap)
            if self.nums[left_swap] == self.nums[first_i]:
                left_swap += 1
            left_i += 1

from copy import copy

p = []
for i in range(100):
    p.append(random.randrange(1, 4))

before = copy(p)

print(p)
Solution(p).sortNums()
print(p)
assert sorted(before) == p
# [1, 1, 2, 2, 3, 3, 3]