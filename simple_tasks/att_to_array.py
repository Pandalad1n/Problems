class Solution:
    def addToArrayForm(self, a, k):
        awns_arr = []
        stringify = ''
        for i in a:
            stringify += str(i)
        awns = str(int(stringify) + k)
        for c in awns:
            awns_arr.append(c)
        return awns_arr

print(Solution().addToArrayForm([1,0,0,0], 1))
