class Solution:
    def duplicateZeros(self, arr) -> None:
        awns = []
        for i in arr:
            if i == 0:
                awns.append(0)
                awns.append(0)
            else:
                awns.append(i)
        awns = awns[:len(arr)]
        arr.clear()
        arr.extend(awns)


arr = [1, 0, 2, 3]
print(arr)
Solution().duplicateZeros(arr)
print(arr)
