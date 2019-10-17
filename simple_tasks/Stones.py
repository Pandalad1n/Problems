class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones.sort()

        while len(stones) > 1:
            stone = stones.pop() - stones.pop()
            if stone != 0:
                stones.append(stone)
                stones.sort()

        return stones[0] if stones else 0


print(Solution().lastStoneWeight([4,3,4,3,2]))
