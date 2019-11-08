class Solution:
    def sortArrayByParity(self, l):
        awns = []
        for i in l:
            if i % 2 != 0:
                awns.append(i)
            else:
                awns.insert(0, i)
        return awns


print(Solution().sortArrayByParity([1, 2, 3, 4]))
